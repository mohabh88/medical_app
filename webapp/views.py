from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db import models
from models import Patient

# Create your views here
def home(request):
    return render_to_response('outline.html')

def patient_info(request):
    return render_to_response('patient_info.html')

def get_patient_id(request):
   try:
       patient_id = request.GET['patient-id']
       mypatient =Patient.objects.get(pk=patient_id)
       return render_to_response('patient_info.html', {"patient": mypatient}, context_instance=RequestContext(request))
   except:
       return HttpResponseRedirect(reverse('patient_info')) 
