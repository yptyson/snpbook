#-*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import admin
import datetime


class Room(models.Model):
    start_time = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    end_time = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    title = models.CharField(max_length=255)
    people_num = models.IntegerField(default=0)
    book_man = models.CharField(max_length=255)
    
    def __unicode__(self):
        return str(self.id)+self.title
 
    class Meta:
        db_table = "room"
        ordering = ['start_time']
class Room_admin(admin.ModelAdmin):
    list_display=('id','title','book_man')
