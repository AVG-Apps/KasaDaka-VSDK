from django.conf.urls import url, include

from . import views

app_name= 'service-development'
urlpatterns = [
    # urls of the voice application
    url(r'^$', views.index, name='index'),
    url(r'^choice/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.choice, name='choice'),
    url(r'^message/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.message_presentation, name='message-presentation'),
    url(r'^start/(?P<voice_service_id>[0-9]+)$', views.voice_service_start, name='voice-service'),
    url(r'^start/(?P<voice_service_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.voice_service_start, name='voice-service'),
    url(r'^user/register/(?P<session_id>[0-9]+)$', views.KasaDakaUserRegistration.as_view(), name = 'user-registration'),
    url(r'^language_select/(?P<session_id>[0-9]+)$', views.LanguageSelection.as_view(), name = 'language-selection'),
    url(r'^record/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.record, name='record'),

    # urls of the own create xml files
    url(r'^voice_app/', views.voice, name='voice'),



    # urls of the web interface

    url(r'^add/fertilizer/$', views.add_fertilizer, name='add_fertilizer'),
    url(r'^add/crop/$', views.add_crop, name='add_crop'),
    url(r'^add/weather/$', views.add_weather, name='add_weather'),
    url(r'^add/tutorial/$', views.add_tutorial, name='add_tutorial'),

    url(r'^fertilizer/(?P<id>\d+)/edit/$', views.edit_fertilizer, name='edit_fertilizer'),
    url(r'^fertilizer/(?P<id>\d+)/delete/$', views.delete_fertilizer, name='delete_fertilizer'),

    url(r'^fertilizer/(?P<id>\d+)/$', views.fertilizer, name='fertilizer'),

    url(r'^fertilizer/', views.main, name='main'),

    url(r'^fertilizer/team/$', views.team, name='team'),



]

