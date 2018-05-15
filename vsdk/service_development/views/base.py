from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse

from ..models.models import Crop

def index(request):
    return HttpResponse('This is the VoiceXML generator')

def redirect_to_voice_service_element(element,session):
    """
    Redirects to a VoiceServiceElement (of unknown subclass), including the session_id in the request.
    """
    return redirect(element._urls_name, element_id = element.id, session_id = session.id)

def redirect_add_get_parameters(url_name, *args, **kwargs):
    """
    Like Django's redirect(), but adds GET parameters at the end of the URL.
    """
    from django.urls import reverse 
    from django.http import HttpResponseRedirect
    import urllib
    url = reverse(url_name, args = args)
    params = urllib.parse.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)

def reverse_add_get_parameters(url_name, *args, **kwargs):
    """
    Like Django's reverse(), but adds GET parameters at the end of the URL.
    """
    from django.core.urlresolvers import reverse 
    import urllib
    url = reverse(url_name, args = args)
    params = urllib.parse.urlencode(kwargs)
    return url + "?%s" % params


#===============================
# WEBSITE MAMOISSON
#===============================

def main(request):
    latest_crop_list = Crop.objects.all()
    context = {'latest_crop_list': latest_crop_list}
    return render(request, 'mamoisson/main.html', context)

def team(request):
    return render(request, 'mamoisson/team.html')

def voice(request):
    latest_crop_list = Crop.objects.all()
    context = {'latest_crop_list': latest_crop_list}
    return render(request, 'main-en-1.xml', context,  content_type='text/xml')