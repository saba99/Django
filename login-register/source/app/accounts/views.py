from base64 import urlsafe_b64encode

from django.conf import settings
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import \
    PasswordChangeView as BasepasswordChangeView
from django.contrib.auth.views import \
    PasswordResetConfirmView as BasePasswordResetConfirmView
from django.contrib.auth.views import \
    PasswordResetDoneView as BasePasswordResetDoneView
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import is_safe_url
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from mysqlx.errorcode import \
    ER_AUDIT_LOG_USER_FIRST_CHARACTER_MUST_BE_ALPHANUMERIC

from .forms import (ChangeEmailForm, ChangeProfileForm, RemindUsernameForm,
                    ResendActivationCodeForm, ResendActivationCodeViaEmailForm,
                    RestorePasswordForm, RestorePasswordViaEmailOUserrnameForm,
                    SignaInViaUsernameForm, SignInViaEmailForm,
                    SignInViaEmailOrUsernameForm, SignUpForm)
from .models import Activation
from .utils import (send_activation_change_email, send_activation_email,
                    send_forgotten_username_email, send_reset_password_email)


class GuestOnlyView(View):
    def  dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
             return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs) 
class LoginView(GuestOnlyView,FormView):

    template_name='accounts/log_in.html'

    @staticmethod 
    def get_form_class(**kwargs):
        if settings.DISABLE_USERNAME or settings.LOGIN_VIA_EMAIL:
            return SignInViaEmailForm 
        if settings.LOGIN_VIA_EMAIL_OR_USERNAME:
            return SignInViaEmailOrUsernameForm 
    @method_decorator(senstive_post_parameters('password')) 
    @method_decorator(csrf_protect) 
    @method_decorator(never_cache) 
    def dispatch(self, request, *args, **kwargs):

        request.sessions.set_test_cookie()
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self,form):
        request=self.request 
    if request.session.test_cookie_worked():

        request.session.delete_test_cookie() 
    if settings.USE_REMEMBER_ME:

        if not form.cleand_data['remember_me']:
            request.session.set_expiry(0)  

    login(request,form.user_cache) 

    redirect_to=request.Post.get(REDIRECT_FIELD_NAME,request.GET.get(REDIRECT_FIELD_NAME))  
    url_is_safe=is_safe_url(redirect_to,allowed_hosts=request.get_host(),require_https=request.is_secure())
    if url_is_safe:
        return redirect(redirect_to) 
    return redirect(settings.LOGIN_REDIRECT_URL)  

class SignUpView(GuestOnlyView,FormView):

    template_name='accounts/sign_up.html'
    form_class=SignUpForm 
    def form_valid(self,form):
        request=self.request 
        user=form.save(Commit=False)
        if settings.DISABLE_USERNAME:
            user.username=get_random_string() 
        else:
            user.username=form.cleand_data['username'] 
        if settings.ENABLE_USER_ACTIVATION:
            user.is_active=False 
        user.save() 
        if settings.DISABLE_USERNAME:
            user.username=f'user_{user.id}'
            user.is_active=False
        if settings.ENABLE_USER_ACTIVATION:
            code= get_random_string(20) 

            act=Activation()
            act.code=code
            act.user=user 
            act.save()  

            send_activation_email(request,user.email,code) 

            messages.success(
                request,_('you are signed up.to activate the account ,follow the link sent to the email  ') )
        else:
                r_password=form.cleand_data['password1']
                user=authenticate(username=user.username,password=r_password)
                login(request,user)
                messages.success(request,_('you are successfully signed up'))
        return redirect('index') 
class ActivateView(View):
    @staticmethod
    def get(request,code):
        act=get_object_or_404(Activation,code=code) 

        user=act.user
        user.is_active=True 
        usersave()   

        act.delete() 
        messages.success(
            request,_('you have successfully activated your account')
        )  
        return redirect('accounts:log_in')     
class ResendActivationCodeView(GuestOnlyView,FormView):

    template_name='accounts/resend_activation_code.html'
    @staticmethod

    def get_form_class(**kwargs):
        if settings.DISABLE_USERNAME:
            return ResendActivationCodeViaEmailForm
        return ResendActivationCodeForm  
    def form_valid(self,form):

        user=form.user_cache 
        activation=user.activation_set.first()  
        activation.delete()

        code=get_random_string(20)

        act=Activation()
        act.code=code
        act.user=user 
        act.save()
        send_activation_email(self.request,user.email,code)
        messages.success(self.request,_('a new activation code has been sent to your email address'))

        return redirect('accounts:resend_activation_code')
class RestorePasswordView(GuestOnlyView,FormView):

    template_name='accounts/restore_password.html'        
    @staticmethod
    def get_form_class(**kwargs):
        if settings.RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME:
            return RestorePasswordForm 
    def form_valid(self,form):

        user=form.user_cache
        token=default_token_generator.make_token(user)
        uid=urlsafe_b64encode(force_bytes(user.pk)).decode()
        send_reset_password_email(self.request,user.email,token,uid)

        return redirect('accounts:restore_password_done')
class ChangeProfileView(LoginRequiredMixin,FormView):
        template_name='accounts/change_profile.html'
        form_class=ChangeProfileForm 

        def get_initial(self):

            user=self.request.user 
            initial=super().get_initial()
            initial['first_name']=user.first_name
            initial['last_name']=user.last_name 
            return initial 
        def form_valid(self,form):
            user=self.request.user 
            user.first_name=form.cleaned_data['first_name'] 
            user.last_name=form.cleaned_data['last_name']
            user.save()   
            messages.success(self.request,_('profile data has been successfully updated'))

        return redirect('accounts:change_profile')
class ChangeEmailView(LoginRequiredMixin,FormView):

    template_name='accounts/profile/change_email.html'  
    form_class=ChangeEmailForm

    def get_form_kwargs(self):

        kwargs=super().get_form_kwargs()
        kwargs['user']=self.request.user 

        return kwargs 
    def get_initial(self):

        initial=super().get_initial() 

        initial['email']=self.request.user.email 

        return initial 
    def form_valid(self,form):

        user=self.request.user

        email=form.cleaned_data['email'] 

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:

            code=get_random_string(20)   

            act=Activation() 

            act.code=code 

            act.user=user 

            act.email=email 
            act.save()

            send_activation_change_email(self.request,email,code) 
            messages.success(self.request,_('to complete the change of email address ,click on link'))
        else:

            user.email=email 
            user.save()  
            messages.success(self.request,_('email successfully changed'))   
        return redirect('accounts:change_email') 

class ChangeEmailActivateView(View):

    @staticmethod 
    def get(request,code):
        act=get_object_or_404(Activation,code=code) 

        user=act.user 
        user.email=act.email 
        user.save()   

        act.delete() 
        messages.success(request,_('you have successfully changed your email')) 
class RemindUsernameView(GuestOnlyView,FormView):

    template_name='accounts/remind_username.html' 
    form_class=RemindUsernameForm 
    def form_valid(self,form):
        user=form.user_cache 
        send_forgotton_email(user.email,user.username) 

        messages.success(self.request,_('your username has been successfully sent to your email'))
    return redirect('accounts:change_password')   

class RestorePasswordConfirmView(BasePasswordResetConfirmView):
     template_name='acccounts/restore_password_confirm.html'

     def form_valid(self,form):

         form.save() 

         login(self.request,user) 

         messages.success(self.request,_('your password has been sent'))

class RestorePasswordDoneView(BasePasswordResetDoneView):

    template_name='accounts/restore_password_done.html'   
class LogOutView(LoginRequiredMixin,BaseLogoutView):

    template_name='accounts/log_out.html'          









