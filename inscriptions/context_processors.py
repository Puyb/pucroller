from django.conf import settings
from django.contrib.sites.models import Site

def import_settings(request):
    return {
        'PAYPAL_URL':      settings.PAYPAL_URL,
        'ROOT_URL': 'http://%s' % Site.objects.get_current(),
        'PAYPAL_BUSINESS': settings.PAYPAL_BUSINESS,
    }
