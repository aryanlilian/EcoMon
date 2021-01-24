from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import NewsletterForm
from .models import Newsletter, Testimonial
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from common.mixins import IsAuthenticatedMixin, SendEmailThreadMixin
from common.constants import messages, template_titles, help_texts

class IndexFormView(IsAuthenticatedMixin, View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, messages['email_exists'])
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, messages['email_subscribed'])
            return redirect('index')
        return render(request, self.template_name)


class AboutTemplateView(IsAuthenticatedMixin, TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_page_title'] = template_titles['about_title']
        context['page_location'] = template_titles['about_path']
        return context


class ContactView(View):
    template_name = 'home/contact.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['email']
        email_host = settings.EMAIL_HOST_USER
        to_email = ['ecomon.services@gmail.com']
        success_message, error_message = None, None
        try:
            email = EmailMessage(
                subject,
                message + '\nsender: ' + from_email,
                email_host,
                to_email,
            )
            SendEmailThreadMixin(email).start()
            success_message = messages['email_received']
        except:
            error_message = messages['fail_sent_email']
        context['success_message'] = success_message
        context['error_message'] = error_message
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
            'banner_page_title': template_titles['contact_title'],
            'page_location': template_titles['contact_path'],
            'comment_email' : help_texts['email'],
            'comment_any_character' : help_texts['any_character']
        }
        return context


class UserResgistrationCreateView(IsAuthenticatedMixin, CreateView):
    template_name = 'home/auth/register.html'
    form_class = UserRegistrationForm


class UserLoginView(IsAuthenticatedMixin, LoginView):
    template_name = 'home/auth/login.html'
