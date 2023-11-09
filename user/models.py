"""
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='userprofile')
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=300, blank=False, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return str(self.name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile, created = (
            UserProfile.objects
            .get_or_create(user=instance)
        )
        # Assign the username as the initial name
        user_profile.name = instance.username
        user_profile.email = instance.email
        user_profile.save()
"""