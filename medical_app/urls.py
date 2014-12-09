from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medical_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'webapp.views.home', name= 'home'),
    url(r'patient_info', 'webapp.views.patient_info', name= 'patient_info'),
    url(r'patient-by-id',  'webapp.views.get_patient_id', name='patient_id'),
    #url(r'get_patient_info', 'webapp.views.get_patient_info', name ='patient info'),
)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
