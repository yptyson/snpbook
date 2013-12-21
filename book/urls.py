#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('book.views',    
    (r'book_list/$', 'book_list'),
    (r'save_borrow/$', 'save_borrow'),
    (r'confirm_share/$', 'confirm_share'),    
    (r'show_return_books/$', 'show_return_books'),
    (r'back_book/$','back_book'),
    (r'list_return_book/$','list_return_book'),
    (r'index/$', 'index'),
    (r'create_book/$', 'create_book'),
    (r'create_one/$', 'create_one'),
)
