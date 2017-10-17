from django.conf.urls import url
from . import views

urlpatterns= [
    #/
    url(r'^$', views.timetable, name= 'timetable'),
    #/rserv/1016
    url(r'^rserv/date(?P<pk>\d{4})$', views.rserv_date, name= 'rserv_date'),
    #rserv/1016/11
    url(r'^rserv/date(?P<rdate>\d{4})/time(?P<pk>\d{2})/room(?P<room>\d{1})$', views.rserv_info, name='rserv_info'),
    #rserv/1016/11/edit
    # url(r'^rserv/date(?P<rdate>\d{4})/(?P<pk>\d{2})/edit$', views.rserv_edit, name= 'rserv_edit'),

]
