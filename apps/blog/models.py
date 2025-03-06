from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)