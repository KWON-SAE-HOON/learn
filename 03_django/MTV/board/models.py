from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    rank = models.IntegerField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

