#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
import urllib2
import json
from django.core.mail import send_mail
import datetime

import MySQLdb
import sys
import os

from django.template.context import RequestContext
reload(sys)                                                 #插入数据库的时候显示中文
sys.setdefaultencoding('utf-8')#编码采用utf-8
from django.contrib.auth import *
from django.contrib.auth.models import User,check_password


def user_login(request):
    '''
    用户登录
    '''
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        print "username:",username1
        print "password:",password1
        try:
            if len(User.objects.filter(username = username1)):
                p = User.objects.get(username__exact = username1)
                if check_password(password1,p.password):
                    print 'check-------ok'
                else :
                    p.set_password(password1)
                    p.save()
                    print 'passowrd -----is ----wrong'
                    return render_to_response('login/login.html', {})
            else:
                print 'new------user---',username1,'----',password1
                new_user = User.objects.create_user(username = username1,email = "a@a.com",password = 'woaixuexi')
                new_user.save()
            user = authenticate(username = username1, password = 'woaixuexi')
            login(request, user)
            return HttpResponseRedirect('/book/book_list/')
        except:
            return render_to_response('login/login.html', {})
    else:
       return render_to_response('login/login.html', {})

# def user_login(request):
#     '''
#     用户登录
#     '''
#     if request.method == "POST":
# #        con = ldap.initialize("ldap://ccldap.chinacache.com:389")
# #        con.set_option(ldap.OPT_X_TLS_DEMAND, True)
# #        con.protocol_version = ldap.VERSION3
#         username1 = request.POST.get('username')
#         password1 = request.POST.get('password')
#         if username1 == 'ccadmin':
#             p = User.objects.get(username__exact = username1)
#             if check_password(password1,p.password):
#                 user = authenticate(username = username1, password = password1)
#                 login(request, user)
#                 return HttpResponseRedirect('/contract/index/')
#         result = ldap_check(username1,password1)
#         try:
#             if result:
#                 if User.objects.filter(username = username1):
#                     p = User.objects.get(username__exact = username1)
#                     p.set_password(password1)
#                     p.save()
#                 user = authenticate(username = username1, password = password1)
#                 login(request, user)
#                 return HttpResponseRedirect('/contract/index/')
#             else:
#                 return render_to_response('login/login.html', {})
#         except Exception,e:
#             return render_to_response('login/login.html', {})
#     else:
#         return render_to_response('login/login.html', {})

# def ldap_check(username,password):
#     con = ldap.initialize("ldap://ccldap.chinacache.com:389")
#     con.set_option(ldap.OPT_X_TLS_DEMAND, True)
#     con.protocol_version = ldap.VERSION3
#     a = con.bind(username,password,ldap.AUTH_SIMPLE)
#     try:
#         result = con.result(a)[0] == 97 and username1 != ""
#         return result
#     except Exception,e:
#         return False


from django.contrib import auth

def user_logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/login/")
# Create your views here.
