from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
   id = models.UUIDField(db_index=True,
                        unique=True,
                        default=uuid.uuid4,
                        editable=False, 
                        primary_key=True)
   
   email = models.EmailField(unique=True, blank=False, null=False)

   