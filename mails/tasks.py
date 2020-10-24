from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from schronisko_krakow.settings import EMAIL_HOST_USER

from .models import EmailTemplate


# this function is handled by CELERY service worker
@shared_task()
def send_email(address):
    """
    Takes an html template and a record from EmailTemplates model and renders to string.
    Creates an instance of EmailMultiAlternatives, populates it with necessary data and calls the 'send' method.
    Then the html template is send to 'address' which is a string argument.
    Returns the string confirmation that email was sent.
    """
    merge_data = {'email': EmailTemplate.objects.first().body}
    subject, from_email, to = 'Testowa wiadomość', EMAIL_HOST_USER, address
    text_content = 'This is an important message.'
    html_content = render_to_string("mails/subscribe-template.html", merge_data)
    message = EmailMultiAlternatives(subject, text_content, from_email, [to])
    message.attach_alternative(html_content, "text/html")
    message.send()
    return "Message was sent"
