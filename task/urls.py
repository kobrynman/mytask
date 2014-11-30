from django.conf.urls import patterns, url

from task import views


urlpatterns = patterns('',
    url(r'^personlist/$', views.person_list, name='person_list'),
    url(r'^newperson/$', views.new_person, name='new_person'),
    url(r'^personlist/(?P<person_id>\d+)/$', views.person_select, name='person_select'),
    url(r'^personlist/(?P<person_id>\d+)/update$', views.update_person, name='update_person'),
    url(r'^personlist/(?P<person_id>\d+)/delete$', views.delete_person, name='delete_person'),

    url(r'^updatedata/', views.update_data, name='update_data'),
    url(r'^findbyphone/', views.find_by_phone, name='find_by_phone'),
)