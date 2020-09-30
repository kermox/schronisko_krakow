from celery import shared_task

from schronisko_krakow.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import EmailTemplates


@shared_task()
def send_email(address):
    merge_data = {'email': EmailTemplates.objects.get().email_body}
    subject, from_email, to = 'Testowa wiadomość', EMAIL_HOST_USER, address
    text_content = 'This is an important message.'
    html_content = render_to_string("mails/adoption-information-email.html", merge_data)
    message = EmailMultiAlternatives(subject, text_content, from_email, [to])
    message.attach_alternative(html_content, "text/html")
    message.send()
    return "Message was sent"
