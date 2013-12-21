#-*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import admin
import datetime


class Book(models.Model):
    name = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    remark = models.CharField(max_length=255,blank=True)
    share = models.IntegerField(default=0)#0不需要分享，1需要分享
    #reward  = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.id)+self.name

    def get_book_user_name(self):
        return self.borrow_set.all()[0].user.first_name
    def get_book_user_borrow_time(self):
        return self.borrow_set.all()[0].borrow_time
    def get_borrow_status(self):    
        if len(self.borrow_set.all()) ==0:
            return 1
        else:            
            i_status = 1
            for i in self.borrow_set.all():                
                if i.return_time is  None:                    
                    i_status = 0
                    break
            return i_status        
    class Meta:
        db_table = "book"
        ordering = ['-id']
class Book_admin(admin.ModelAdmin):
    list_display=('id','name','writer','remark','share')

def get_books():
    return Book.objects.all()
def create_one_book(request_post):
	Book.objects.create(name=request_post.get('name'),writer=request_post.get('writer'),share= request_post.get('share'))	
        
class Borrow(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    borrow_time = models.DateField(null=True,blank=True)
    return_time = models.DateField(null=True,blank=True)
    share_status = models.IntegerField(default=0)#0不需要分享，1未分享，2分享完
    #objects = models.Manager()
    #return_book = Return_book()
    
    def __unicode__(self):
        return str(self.id)+str(self.user.id)+self.book.name
    def confirm_share(self):
        self.share_status = 2
        self.save()
        
    def get_borrow_period(self):        
        return (self.return_time - self.borrow_time).days    
        
    def get_keep_period(self):               
        return 30-(datetime.datetime.now().date() - self.borrow_time).days
        
    class Meta:
        db_table = "borrow"
        #unique_together = (("user", "book"),)
        ordering = ['-borrow_time']

class Borrow_admin(admin.ModelAdmin):
    list_display=('id','book','borrow_time','return_time')
    
def get_all_borrow1():
    return Borrow.objects.filter(return_time__isnull=False)
    
def get_all_borrow2():
    return Borrow.objects.filter(return_time__isnull=True)

def save_borrow_object(request_get):
    book_id = request_get.get('book_id')
    user_id = request_get.get('user_id')
    book_obj = Book.objects.get(id=book_id)
    borrow_obj = Borrow.objects.create(user=User.objects.get(id=user_id),book=book_obj,borrow_time = datetime.datetime.now().date())
    if book_obj.share == 1 :
        borrow_obj.share_status = 1
        borrow_obj.save()

def save_back_book(request_get):
    borrow_id = request_get.get("bookid")
    b_obj = Borrow.objects.get(id=borrow_id)
    b_obj.return_time = datetime.datetime.now()
    b_obj.save()
    
def get_all_book2():
    unborrow, borrow=[], []
    for book in Book.objects.all():        
        if len(book.borrow_set.all())==0:
            unborrow.append(book)
        else:   
            borrow_status = 1         
            for book_item in book.borrow_set.all():
                if book_item.return_time is  None:                    
                    borrow_status = 0
            if borrow_status:
                unborrow.append(book)            
            else:               
                borrow.append(book)     
    return unborrow+borrow    
    
    
    
    
    
    
    
    
    
    

