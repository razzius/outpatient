from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from app.views import sms, Register, welcome

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^register/$', Register.as_view()),
    url(r'^welcome/$', welcome),
    url(r'sms', sms),
    # Examples:
    # url(r'^$', 'outpatient.views.home', name='home'),
    # url(r'^outpatient/', include('outpatient.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
