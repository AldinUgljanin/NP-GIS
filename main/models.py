from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(null=True, upload_to="images/")
    longitude = models.FloatField(
            validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
            )
    latitude = models.FloatField(
            validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
            )

    def __str__(self):
        return f"{self.title} \n {self.description}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} \n {self.name}"
