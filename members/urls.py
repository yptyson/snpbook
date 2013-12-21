#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('members.views',    
    (r'member_list/$', 'member_list'),
 
)
