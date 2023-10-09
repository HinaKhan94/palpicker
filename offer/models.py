from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime, timedelta

# status zero as draft and 1 as published for offer
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Model for offer listings.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="offer_posts")
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
