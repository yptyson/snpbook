#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.template import RequestContext
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
import datetime

from models import Book, Borrow, get_books, save_borrow_object,  get_all_borrow1, get_all_borrow2, create_one_book
from models import get_all_book2
from django.db.models import Count
from django.contrib.auth.models import User
from models import save_back_book
from django.core.context_processors import csrf

def index(request):    
    data = {}
    return render_to_response('book/index.html', data)
    
def book_list(request):    
    data = {'books': get_all_book2()}
    return render_to_response('book/book_list.html', data, context_instance=RequestContext(request))

def save_borrow(request):
    save_borrow_object(request.GET)    
    return redirect(reverse('book.views.show_return_books', args=[]))

def confirm_share(request):    
    borrow_obj = Borrow.objects.get(id=request.GET.get('borrow_id'))
    borrow_obj.confirm_share()
    return redirect(reverse('book.views.show_return_books', args=[]))

def show_return_books(request):    
    data = {'borrowed_books':get_all_borrow2()}
    return render_to_response('book/borrowed_books.html', data, context_instance=RequestContext(request))

def back_book(request):
    save_back_book(request.GET)
    return redirect("/book/list_return_book/")
    
def list_return_book(request):    
    data = {'books': get_all_borrow1()}
    return render_to_response('book/index2.html', data, context_instance=RequestContext(request))

def create_book(request):
	
	date ={}
	return render_to_response('book/create_book.html', date)
	 
def create_one(request):
	create_one_book(request.POST)
	return redirect("/book/book_list/")
    
    
    
    
#~ from django.core.cache import cache    
#~ def get_my_cache(request):
    #~ data = {'name':"yeyi"}
    #~ cache.set('cache_key',data,60*1)
     #~ #cache_key为存储在缓存中的唯一值，data为存储的数据，60*15为缓存数据的时间#获取缓存数据
    #~ print 'my_cache::::::',cache.get('cache_key',None)#cache_key为储存缓存数据的唯一值
    #~ cache.set('cache_key',data,60*1)
    #~ 
    #~ return render_to_response("book/get_my_cache.html",{})    
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
