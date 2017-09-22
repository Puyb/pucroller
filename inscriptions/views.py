# -*- coding: utf-8 -*-
import sys, requests, random, json
import logging
from datetime import datetime, date
from functools import reduce
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Count, Sum, Min, F, Q, Prefetch
from django.db.models.functions import Coalesce
from django.db.models.query import prefetch_related_objects
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, Template, Context
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.utils import timezone
from django.utils.http import urlencode
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from .forms import MembreForm
from .models import Membre, Saison
from .utils import MailThread, jsonDate
from decimal import Decimal

logger = logging.getLogger(__name__)
def get_saison(offset=0):
    today = datetime.today()
    year = today.year + offset
    if today.month < 7:
        year = year - 1
    print(Saison.objects.all(), year)
    return Saison.objects.get(annee=year)


def reinscription(request):
    if request.method == 'POST':
        try:
            #instance = Membre.objects.filter(Q(num_licence=request.POST['q']) | Q(email__iexact=request.POST['q'])).filter(saison=get_saison(-1))[0]
            instance = Membre.objects.filter(Q(num_licence=request.POST['q']) | Q(email__iexact=request.POST['q'])).filter(saison=get_saison(-1))[0]
            return redirect(reverse('inscriptions.inscription') + '?id=%d' % instance.id)
        except Exception as e:
            print(e)
            return render_to_response("reinscription.html", RequestContext(request, {
                'message': "Impossible de trouver votre licence sur l'année écoulée. Vérifier votre numéro de licence",
            }))
    return render_to_response("reinscription.html", RequestContext(request, {
    }))

@transaction.atomic
def inscription(request):
    saison = get_saison()
    instance = None
    previousinstance = None
    old_password = None
    if request.method == 'POST':
        form = MembreForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.password = old_password
            if not instance:
                new_instance.password = '%06x' % random.randrange(0x100000, 0xffffff)

            new_instance.prix = Decimal(180)
            if date.today() <= date(date.today().year, 10, 15) and Membre.objects.filter(num_licence=new_instance.num_licence, saison=get_saison(-1)).count():
                new_instance.prix -= Decimal(10)
            if new_instance.reduction in ('chomeur', 'etudiant'):
                new_instance.prix = Decimal(140)
            if new_instance.autre_club:
                new_instance.prix -= Decimal(35)
            
            new_instance.saison = saison
            new_instance.save()
            if not instance:
                try:
                    # send mail
                    pass
                except Exception as e:
                    logging.exception('Fail to send "inscription" mail')
            response = redirect('inscriptions.done', id=new_instance.id)
            response.set_cookie(new_instance.cookie_key(), new_instance.password, max_age=365*86400, httponly=True)
            return response
        else:
            text = 'Error in form submit\n'
            text += request.META['REMOTE_ADDR'] + '\n'
            text += request.path + '\n'
            text += json.dumps(form.errors) + '\n'
            text += json.dumps(request.POST)
            mail = EmailMessage('Error in form submit', text, settings.DEFAULT_FROM_EMAIL, [ settings.SERVER_EMAIL ], reply_to=[])
            mail.content_subtype = "text"
            MailThread([ mail ]).start()
    else:
        if 'id' in request.GET:
            previousinstance = get_object_or_404(Membre, id=request.GET['id'])
        form = MembreForm(instance=previousinstance)

    return render_to_response("form.html", RequestContext(request, {
        "form": form,
        "errors": form.errors,
        "previous": previousinstance,
    }))

def done(request, id):
    try:
        instance = Membre.objects.get(id=id)
        ctx = RequestContext(request, {
            "instance": instance,
            "paypal_ipn_url": request.build_absolute_uri(reverse('inscriptions.ipn')),
            "hour": datetime.now().strftime('%H%M'),
        })
        return render_to_response('done.html', ctx)
    except Membre.DoesNotExist as e:
        raise Http404()


@csrf_exempt
def ipn(request):
    """PayPal IPN (Instant Payment Notification)
    Cornfirms that payment has been completed and marks invoice as paid.
    Adapted from IPN cgi script provided at http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/456361"""

    try:
        if not confirm_ipn_data(request.body.decode('ascii'), settings.PAYPAL_URL):
            logger.warning('Reject ipn %s', json.dumps(request.POST))
            return HttpResponse()

        data = request.POST
        if not 'payment_status' in data or not data['payment_status'] == "Completed":
            # We want to respond to anything that isn't a payment - but we won't insert into our database.
            logger.warning('ipn is not a payment %s', json.dumps(request.POST))
            return HttpResponse()

        membre = get_object_or_404(Membre, id=data['invoice'][0:-4])
        membre.paiement = data['mc_gross']
        membre.paiement_info = 'Paypal %s %s %s %s %s' % (datetime.now(), data['txn_id'], data['payer_email'], data['first_name'], data['last_name'])
        membre.save()

    except:
        logger.exception('error handling paypal ipn')

    return HttpResponse()

def confirm_ipn_data(data, PP_URL):
    # data is the form data that was submitted to the IPN URL.
    #PP_URL = 'https://www.paypal.com/cgi-bin/webscr'

    params = data + '&' + urlencode({ 'cmd': "_notify-validate" })

    response = requests.post(PP_URL, params, headers={ "Content-type": "application/x-www-form-urlencoded" })

    if response.text == "VERIFIED":
        logger.debug("PayPal IPN data verification was successful %s.", data)
    else:
        logger.debug("PayPal IPN data verification failed %s.", data)
        return False

    return True

