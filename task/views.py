#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.template import RequestContext
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
import datetime
from models import Task, get_unsolved_task, get_soved_task, get_task_by_id


from django.db.models import Count


def index(request):
    data = {'tasks':get_unsolved_task()}
    return render_to_response('task/index.html', data)
def show_detail_task(request):
    data ={'item':get_task_by_id(request.GET.get('task_id'))}
    return render_to_response('task/show_detail_task.html', data, context_instance=RequestContext(request))    
def show_soved_task(request):    
    data = {'tasks': get_soved_task()}
    return render_to_response('task/show_soved_task.html', data, context_instance=RequestContext(request))# Create your views here.

def create_task(request):
	data = {}
	return render_to_response('task/create_task.html', data, context_instance=RequestContext(request))

def task_save(request):
    data = {}
    request.POST.get('')
    Task.objects.create(request.POST.get(''),request.POST.get(''))
    return redirect(reverse('task.views.show', args=[]))	

def month_winner(request):
	data = {'objects': get_month_winner()}
	return render_to_response('task/month_winner.html', data, context_instance=requestContext(request))

# def show_new_task(request):
# 	data = {'objects': get_new_task}
# 	return render_to_response('task/show_new_task.html', data, context_instance=requestContext(request))

# def show_soved_task(request):
#     data = {'objects': get_soved_task}
#     return render_to_response('task/show_soved_task.hmtl', data, context_instance=requestContext(request))

# def send_task_mails(request):
#     send_mails    	




