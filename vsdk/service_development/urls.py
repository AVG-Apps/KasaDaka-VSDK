from django.conf.urls import url, include

from . import views

app_name= 'service-development'
urlpatterns = [
    # urls of the voice application
    url(r'^admin/$', views.index, name='index'),
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

    #TUTORIALS URLS
    url(r'^tutorial/add/$', views.add_tutorial, name='add_tutorial'),
    url(r'^tutorial/(?P<id>\d+)/edit/$', views.edit_tutorial, name='edit_tutorial'),
    url(r'^tutorial/(?P<id>\d+)/delete/$', views.delete_tutorial, name='delete_tutorial'),
    url(r'^tutorial/$', views.overview_tutorial, name='overview_tutorial'),

    #CATEGORY URLS
    url(r'^category/add/$', views.add_category, name='add_category'),
    url(r'^category/(?P<id>\d+)/edit/$', views.edit_category, name='edit_category'),
    url(r'^category/(?P<id>\d+)/delete/$', views.delete_category, name='delete_category'),
    url(r'^category/$', views.overview_category, name='overview_category'),

    #FERTILIZER URLS
    url(r'^fertilizer/add/$', views.add_fertilizer, name='add_fertilizer'),
    url(r'^fertilizer/(?P<id>\d+)/edit/$', views.edit_fertilizer, name='edit_fertilizer'),
    url(r'^fertilizer/(?P<id>\d+)/delete/$', views.delete_fertilizer, name='delete_fertilizer'),
    url(r'^fertilizer/$', views.overview_fertilizer, name='overview_fertilizer'),

    #CROP URLS
    url(r'^crop/add/$', views.add_crop, name='add_crop'),
    url(r'^crop/(?P<id>\d+)/edit/$', views.edit_crop, name='edit_crop'),
    url(r'^crop/(?P<id>\d+)/delete/$', views.delete_crop, name='delete_crop'),
    url(r'^crop/(?P<id>\d+)/$', views.detail_crop, name='detail_crop'),

    #MAIN PAGES
    url(r'^$', views.main, name='main'),
    url(r'^team/$', views.team, name='team'),



]

