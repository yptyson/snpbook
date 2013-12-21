#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.template import RequestContext
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
import datetime



from django.db.models import Count


def index(request):    
    data = {}
    return render_to_response('task/index.html', data)
    