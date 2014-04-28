#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime
from datetime import timedelta


from models import Room

def get_days():
    days_list = []
    today = datetime.datetime.now()
    while(len(days_list)<6):
        if  (today+datetime.timedelta(1)).isoweekday() in [1,2,3,4,5]:            
            days_list.append({'date':today+datetime.timedelta(1),
                              'bookings':Room.objects.filter(start_time__startswith=(today+datetime.timedelta(1)).date())}
                              )            
        today = today+datetime.timedelta(1)
    return {'rooms': days_list}
    #return data
def index(request):

    days_list = []
    today = datetime.datetime.now()
    while(len(days_list)<6):
        if  (today+datetime.timedelta(1)).isoweekday() in [1,2,3,4,5]:            
            days_list.append({'date':today+datetime.timedelta(1),
                              'bookings':Room.objects.filter(start_time__startswith=(today+datetime.timedelta(1)).date())}
                              )            
        today = today+datetime.timedelta(1)
    data = {'rooms': days_list}
    
    return render_to_response('room/index.html', data)

def room_detail(request):
    def roomsave(start, end, title, people_num):
        room_obj = Room(start_time=start, end_time=end, title=title,people_num=people_num,book_man="苑鹏")
        room_obj.save()        
    if request.method == 'POST':    
        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        start = date+' '+starttime+":00"
        end = date+' '+endtime+":00"
        day = datetime.datetime.strptime(date,"%Y-%m-%d").date()
        starttime1 = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        endtime1 = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
        
        if len(Room.objects.filter(start_time__startswith=day)) == 0:            
            roomsave(start, end, request.POST.get('title'), request.POST.get('people_num'))            
        else:            
            if len(Room.objects.filter(start_time__startswith=day,start_time__lte=start)) == 0:
                la_time_obj = Room.objects.filter(start_time__startswith=day,start_time__gte=start)[0]
                if endtime1 <= la_time_obj.start_time:                  
                    roomsave(start, end, request.POST.get('title'), request.POST.get('people_num'))              
            elif len(Room.objects.filter(start_time__startswith=day,start_time__gte=start)) == 0:                
                pr_time_obj = Room.objects.filter(start_time__startswith=day,start_time__lte=start).reverse()[0]
                if starttime1 >= pr_time_obj.end_time:
                    roomsave(start, end, request.POST.get('title'), request.POST.get('people_num'))                                  
            else:
                pr_time_obj = Room.objects.filter(start_time__startswith=day,start_time__lte=start).reverse()[0]
                la_time_obj = Room.objects.filter(start_time__startswith=day,start_time__gte=start)[0]
                if starttime1 >= pr_time_obj.end_time and endtime1 <= la_time_obj.start_time:
                    roomsave(start, end, request.POST.get('title'), request.POST.get('people_num'))
                    
        data = {'date': date ,'booktime': Room.objects.filter(start_time__startswith=day),'days':get_days()}
        return redirect('/room/room_detail/?date=%s'%(date))                        
    else:
        date = request.GET.get('date')
        day = datetime.datetime.strptime(date,"%Y-%m-%d").date()        
        data = {'date': date ,'booktime': Room.objects.filter(start_time__startswith=day)}#.update(get_days())
        data.update(get_days())
        return render_to_response('room/day_detail.html', data)

def delete_booking(request): 
    Room.objects.get(id=request.POST.get('booking_id')).delete()    
    return redirect('/room/room_detail/?date=%s'%(request.POST.get('date')))


def color(request):

    return render_to_response('room/color.html', {})
    
    
    
    
    
    
