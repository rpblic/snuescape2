from django.conf.urls import url
from . import views

urlpatterns= [
    #/
    url(r'^$', views.timetable, name= 'timetable'),
    #rserv/1016/11
    url(r'^rserv/\d{4}/\d{2}$', views.rserv_info, name='rserv_info'),
    url(r'^rserv/\d{4}/\d{2}/edit$', views.rserv_edit, name= 'rserv_edit'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name= 'post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name= 'post_edit')
]
