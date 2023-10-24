from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=False, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=300, blank=False, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.ImageField(upload_to='users/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    
    def __str__(self):
        return str(self.username)
    
    @property
    def profile_img(self):
        if self.profile_image:
            url = self.profile_image.url
        else:
            url = (
                settings.STATIC_URL +
                'images/users/user-default.webp'
            )
        return url
    


