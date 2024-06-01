from django.db import models
from users.models import CustomUser
import uuid
# Create your models here.

class Friends(models.Model):
    id = models.UUIDField(db_index=True,
                        unique=True,
                        default=uuid.uuid4,
                        editable=False, 
                        primary_key=True)
    user1= models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='friend1')
    user2=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='friend2')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1} and {self.user2}"
    

class FriendRequests(models.Model):
    id = models.UUIDField(db_index=True,
                        unique=True,
                        default=uuid.uuid4,
                        editable=False, 
                        primary_key=True)
    from_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sent_request')
    to_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='recieved_request')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user} to {self.to_user} - {self.status}"
