from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    
    url(r'^admin/', include(admin.site.urls)),
    #login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #home 
    url(r'^home/$', views.home),

)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


                        
