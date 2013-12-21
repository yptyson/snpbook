# Create your views here.
#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.template import RequestContext
from django.http import HttpResponse
import json
from room.models import Room

def output(request):
    data = {'info':[]}
    for room in Room.objects.all():
        data['info'].append({'titlea':room.title})

    return HttpResponse(json.dumps(data))