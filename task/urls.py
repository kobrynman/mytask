from django.conf.urls import patterns, url

from task import views


urlpatterns = patterns('',
    url(r'^personlist/$', views.person_list, name='person_list'),
    url(r'^personlist/(?P<person_id>\d+)/$', views.person_select, name='personSelect'),
    #url(r'^addperson/$', views.add_person, name='add_person'),
)