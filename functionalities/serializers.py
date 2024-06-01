from rest_framework import serializers
from .models import Friends,FriendRequests
from users.serializers import CustomUserSerializer  

class FriendsSerializer(serializers.ModelSerializer):
    user1 = CustomUserSerializer (read_only=True)
    user2 = CustomUserSerializer (read_only=True)

    class Meta:
        model = Friends
        fields = ['id', 'user1', 'user2', 'created']


class FriendRequestsSerializer(serializers.ModelSerializer):
    from_user = CustomUserSerializer (read_only=True)
    to_user = CustomUserSerializer (read_only=True)

    class Meta:
        model = FriendRequests
        fields = ['id', 'from_user', 'to_user', 'status', 'timestamp']

