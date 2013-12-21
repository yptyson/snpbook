#-*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import admin
import datetime


class Member(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    home = models.CharField(max_length=255,blank=True)
    nick_name = models.CharField(max_length=255,blank=True)
    department = models.CharField(max_length=255)
    describe = models.CharField(max_length=255,blank=True)
    photo =  models.ImageField(upload_to='photo',null=True,blank=True)


    def __unicode__(self):
        return str(self.id)+self.name

    class Meta:
        db_table = "member"
        ordering = ['id']
class Member_admin(admin.ModelAdmin):
    list_display=('id','name','home')

#~ def get_books():
    #~ return Book.objects.all()
#~ def create_one_book(request_post):
    #~ Book.objects.create(name=request_post.get('name'),writer=request_post.get('writer'),share= request_post.get('share'))

