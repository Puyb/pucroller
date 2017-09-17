import logging
import re
import time
from urllib.parse import urlparse, urlunparse
from threading import Thread
from django.contrib import messages
#from django.template.loader import render_to_string
#from django.core.mail import EmailMessage

logger = logging.getLogger(__name__)

def urlEncodeNonAscii(b):
    return re.sub(b'[\x80-\xFF]', lambda c: ('%%%02x' % ord(c.group(0))).encode('ascii'), b)

def iriToUri(iri):
    parts = urlparse(iri)
    return urlunparse([
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    ])

class MailThread(Thread):
    def __init__ (self, mails):
        Thread.__init__(self)
        self.mails = mails

    def run(self):  
        for mail in self.mails:
            mail.send()

def jsonDate(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))
