from django.db import models

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class UserBlog(models.Model):
    blogheader = models.CharField(max_length=100)
    blog = models.CharField(max_length=500)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)