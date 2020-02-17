from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

def send_mail(to,template,context):
    html_content=render_to_string(f'accounts/emails/(template).html',context)
    text_content=render_to_string(f'accounts/emails/(template).txt',context) 
    msg=EmailMultiAlternatives(context['subject'],text_content,settings.DEFAULT_FORM_EMAIL,[to])
    msg.attach_alternative(html_content,'text/html')
    msg.send() 
def send_activation_email(request) :

    context={
        'subject':_('profile activation'),
        'uri':request.build_absolute_uri(reverse('accounts:activate'))
    }  
    send_mail(email,'activate_profile',context) 

def send_activation_change_email(request,email,code):
      context={
        'subject':_('change email'),
        'uri':request.build_absolute_uri(reverse('accounts:change_email_activation',kwargs={'code':code})),
      }
      send_email(email,'change_email',context) 

def   send_reset_password_email(request,email,token,uid):
    context={
        'subject':_('restore password'),
        'uri': request.build_absolute_uri(reverse('accounts:restore_password_confirm', kwargs={'uid64': uid,'token':token})),
    } 
    send_email(email,'restore_password_email',context) 

def send_forgotten_username_email(email,username):
    context = {
        'subject': _('your username'),
        'username':username,
    }
    send_mail(email,'forgotten_username',context)
       
