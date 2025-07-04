from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    title          = models.CharField(max_length=128)
    text           = models.TextField(blank=True)
    author         = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date   = models.DateTimeField(auto_now_add=True)
    modified_date  = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
