from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.
class SchoolManager(models.Manager):
    def add(self, postData):
        Schools.objects.create(school_name=postData['school_name'],
                               city=postData['city'])

class CommentsManager(models.Manager):
    def add(self, postData):
        school = Schools.objects.get(id=id)
        Comments.objects.create(name=request.session['full_name'],
                                comment=request.POST['comment'],
                                school=school)

class Schools(models.Model):
    school_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SchoolManager()

class Comments(models.Model):
    comment = models.TextField(max_length=1000)
    name = models.TextField(max_length=100)
    comment_creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    school = models.ForeignKey(Schools)
    objects = CommentsManager()
