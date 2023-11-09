from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from datetime import datetime, timedelta
from django.utils import timezone
#from user.models import UserProfile

# status zero as draft and 1 as published for offer
STATUS = ((0, "Draft"), (1, "Published"))
STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Completed', 'Completed'),
    )


class Post(models.Model):

    """
    Model for offer listings.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="offer_posts")
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Request(models.Model):

    """
    Model for requesting an offer to be used by the user
    Fields added to notify the user when the request
    status is changed
    """
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100,
                             verbose_name="Enter customer's contact number",)
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES,
                              default='Pending')
    user_id = models.IntegerField(blank=True, default='0')
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name