from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import NewsletterForm
from .models import Newsletter, Testimonial
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from users.mixins import IsAuthenticatedMixin

class IndexFormView(IsAuthenticatedMixin, View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, 'This email is already subscribed in our system')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'Your email was subscribed in our system, you\'ll hear from us as soon as possible !')
        return render(request, self.template_name)


class AboutTemplateView(IsAuthenticatedMixin, TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_page_title'] = 'About Us'
        context['page_location'] = 'home / about'
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
            send_mail(
                subject,
                message + '\nsender: ' + from_email,
                email_host,
                to_email,
                fail_silently=False
            )
            success_message = 'We\'ve received your email, you\'ll hear from us very soon!'
        except:
            error_message = 'Something didn\'t work, please try later!'
        context['success_message'] = success_message
        context['error_message'] = error_message
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
            'banner_page_title': 'Contact',
            'page_location': 'home / contact'
        }
        return context


class UserResgistrationCreateView(IsAuthenticatedMixin, CreateView):
    template_name = 'home/auth/register.html'
    form_class = UserRegistrationForm


class UserLoginView(IsAuthenticatedMixin, LoginView):
    template_name = 'home/auth/login.html'
