#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('room.views',    
    (r'index/$', 'index'),
    (r'room_detail/$', 'room_detail'),
    (r'delete_booking/$', 'delete_booking'),
    
    #(r'color/$', 'color'),
    #(r'room_detailw/(?P<date>\w+)/$', 'room_detail'),
    #(?P<poll_id>\d+)/
)
