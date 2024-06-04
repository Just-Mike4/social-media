from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.throttling import UserRateThrottle
from .models import Friends,FriendRequests
from users.models import CustomUser
from .serializers import FriendsSerializer,FriendRequestsSerializer
from users.serializers import CustomUserSerializer

class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    

    def get_queryset(self):
        keyword = self.request.query_params.get('search', '')
        return CustomUser.objects.filter(Q(email__iexact=keyword) | Q(username__icontains=keyword)).distinct()

class FriendRequestThrottle(UserRateThrottle):
    rate = '3/min'

class FriendRequestsViewSet(viewsets.ModelViewSet):
    serializer_class = FriendRequestsSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [FriendRequestThrottle]
    http_method_names = ['get', 'post', 'patch']

    def create(self, request, *args, **kwargs):
        to_username = request.data.get('to_username')

        try:
            to_user = CustomUser.objects.get(username=to_username)
        except CustomUser.DoesNotExist:
            return Response({"detail": "CustomUser not found."}, status=status.HTTP_404_NOT_FOUND)

        friend_request, created = FriendRequests.objects.get_or_create(
            from_user=request.user,
            to_user=to_user,
        )
        if not created:
            return Response({"detail": "Friend request already sent."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(FriendRequestsSerializer(friend_request).data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        friend_request_id = kwargs.get('pk')
        action = request.data.get('action')
        try:
            friend_request = FriendRequests.objects.get(id=friend_request_id, to_user=request.user)
        except FriendRequests.DoesNotExist:
            return Response({"detail": "Friend request not found."}, status=status.HTTP_404_NOT_FOUND)

        if action == 'accept':
            friend_request.status = 'accepted'
            Friends.objects.create(user1=request.user, user2=friend_request.from_user)
        elif action == 'reject':
            friend_request.status = 'rejected'
        else:
            return Response({"detail": "Invalid action."}, status=status.HTTP_400_BAD_REQUEST)

        friend_request.save()
        return Response(FriendRequestsSerializer(friend_request).data)
    
    def get_queryset(self):
        queryset = FriendRequests.objects.filter(to_user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FriendsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    

    def get_queryset(self):
        user = self.request.user
        friends = Friends.objects.filter(Q(user1=user) | Q(user2=user))
        friend_ids = [f.user1.id if f.user2 == user else f.user2.id for f in friends]
        return CustomUser.objects.filter(id__in=friend_ids)
