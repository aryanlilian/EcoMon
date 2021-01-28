from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import NewsletterForm
from .models import Newsletter, Testimonial
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from common.mixins import IsAuthenticatedMixin, SendEmailThreadMixin
from common.constants import messages_text, template_titles, help_texts

class IndexFormView(IsAuthenticatedMixin, View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('newsletter_email')
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, messages_text['email_exists'])
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, messages_text['email_subscribed'])
            return redirect('index')
        return render(request, self.template_name)


class AboutTemplateView(IsAuthenticatedMixin, TemplateView):
    template_name = 'home/about.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        email = request.POST.get('newsletter_email')
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, messages_text['email_exists'])
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, messages_text['email_subscribed'])
            return redirect('about')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_page_title'] = template_titles['about_title']
        context['title'] = template_titles['about_title']
        context['page_location'] = template_titles['about_path']
        return context


class ContactView(View):
    template_name = 'home/contact.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.POST.get('email')
        success_message, error_message = None, None
        email = request.POST.get('newsletter_email')
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, messages_text['email_exists'])
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, messages_text['email_subscribed'])
            return redirect('contact')
        if subject and message and email:
            try:
                send_mail(
                    subject,
                    message + '\nsender: ' + from_email,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False
                )
                success_message = messages_text['email_received']
            except:
                error_message = messages_text['fail_sent_email']
        context['success_message'] = success_message
        context['error_message'] = error_message
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
            'banner_page_title': template_titles['contact_title'],
            'title' : template_titles['contact_title'],
            'page_location': template_titles['contact_path'],
            'comment_email' : help_texts['email'],
            'comment_any_character' : help_texts['any_character']
        }
        return context


class UserResgistrationCreateView(IsAuthenticatedMixin, SuccessMessageMixin, CreateView):
    template_name = 'home/auth/register.html'
    form_class = UserRegistrationForm
    success_message = 'Account created successfully for "%(username)s"'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context


class UserLoginView(IsAuthenticatedMixin, LoginView):
    template_name = 'home/auth/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
