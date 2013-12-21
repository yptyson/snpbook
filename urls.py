from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
#from django.contrib.auth.views import login,logout
from django.contrib.auth.views import login,logout


urlpatterns = patterns('',
     #(r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),

     (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_PATH}),
     (r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_PATH}),
     (r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_PATH}),

     (r'^admin/', include(admin.site.urls)),
     (r'^book/',include('book.urls')),
     (r'^room/',include('room.urls')),
     (r'^member/',include('members.urls')),
     (r'^task/',include('task.urls')),
     (r'^blog/',include('blog.urls')),
     (r'^interface/',include('interface.urls')),
     (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_PATH}),
     (r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_PATH}),
     (r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_PATH}),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
urlpatterns +=patterns('login.views',
    (r'^login/$','user_login'),
    (r'^logout/$','user_logout'),
    (r'^accounts/login/$','user_login'),

    (r'^$','user_login'),
)

#~ urlpatterns +=patterns('login.views',
    #~ (r'^$','user_login'),
    #~ #(r'^login/$','sso_login'),
    #~ #(r'^sso_login/$','sso_login'),
    #~ #(r'^accounts/login/$','sso_login'),
    #~ #(r'^logout/$','user_logout'),
#~ )

