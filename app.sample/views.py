# Views for app '{{ app_name }}'
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def home(request):
    return render_to_response(
        '{{ app_name }}_sample.html',
        {'name': 'Works!'},
        context_instance=RequestContext(request)
    )

