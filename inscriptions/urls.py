from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import ListView

from inscriptions import admin


urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^reinscription/$', 'inscriptions.views.reinscription', name='inscriptions.reinscription'),
    url(r'^inscription/$', 'inscriptions.views.inscription', name='inscriptions.inscription'),
    url(r'^inscription/(?P<id>\d+)/done/$', 'inscriptions.views.done', name='inscriptions.done'),
    url(r'^inscription/ipn/$', 'inscriptions.views.ipn', name='inscriptions.ipn'),
    url(r'^membres/(?P<saison>\d+)-\d+/trombi/$', 'inscriptions.views.list', name='inscriptions.trombi'),
]

