from django.db import models


class Thread(models.Model):
    title = models.CharField(max_length=255)
    contributor_name = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    thread = models.ForeignKey(Thread)
    contributor_name = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
