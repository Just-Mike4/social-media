from django.contrib import admin
from .models import Friends,FriendRequests
# Register your models here.

admin.site.register(Friends)
admin.site.register(FriendRequests)