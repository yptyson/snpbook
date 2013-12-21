#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.template import RequestContext
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
import datetime
from models import Member



def member_list(request):    
   
    
   
    member_list = Member.objects.all()
    data ={'members':member_list}
    print data,'---------------'
    
    return render_to_response('member/index.html', data, context_instance=RequestContext(request))
    
