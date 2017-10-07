from django.conf.urls import url
from . import views

urlpatterns= [
    #/
    url(r'^$', views.timetable, name= 'timetable'),
    #/rserv/1016
    url(r'^rserv/(?P<pk>\d{4})$', views.rserv_date, name= 'rserv_date'),
    #rserv/1016/11
    url(r'^rserv/(?P<rdate>\d{4})/(?P<pk>\d{2})$', views.rserv_info, name='rserv_info'),
    #rserv/1016/11/edit
    url(r'^rserv/(?P<rdate>\d{4})/(?P<pk>\d{2})/edit$', views.rserv_edit, name= 'rserv_edit'),

    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name= 'post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name= 'post_edit')
]
