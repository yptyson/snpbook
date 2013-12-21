#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('task.views',    
    (r'index/$', 'index'),
    (r'show_soved_task/$','show_soved_task'),
    (r'create_task/$','create_task'),
    (r'show_detail_task/$','show_detail_task'),
)
