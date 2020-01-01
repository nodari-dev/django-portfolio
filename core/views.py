from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView

def home(request):
	return render(request=request, template_name="index.html")
def about(request):
	return render(request=request, template_name="about.html")

# def handler404(request, *args, **argv):
#     response = render_to_response('404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response
#
#
# def handler500(request, *args, **argv):
#     response = render_to_response('500.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response