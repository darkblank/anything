from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
