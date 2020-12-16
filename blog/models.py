from django.db import models

class blog(models.Model):
    name = models.CharField(max_length=64)

class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.TextField(default ="teehee")
    def __str__(self):
        return f'{self.title}, {self.author}'