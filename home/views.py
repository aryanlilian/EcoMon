from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import NewsletterForm
from .models import Newsletter, Testimonial
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexFormView(CreateView):
    template_name = 'home/index.html'
    form_class = NewsletterForm

    def post(self, request, *args, **kwargs):
        if Newsletter.objects.filter(email=request.POST['email']).exists():
            messages.warning(
                request, 'This email is already subscribed in our system')
        else:
            Newsletter.objects.create(
                email=request.POST['email'])
            messages.success(request,
                             'Your email was subscribed in our system, you\'ll hear from us as soon as possible !')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.order_by(
            '-created_date')[:9]
        return context


class AboutTemplateView(TemplateView):
    template_name = 'home/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'home/contact.html'


class UserResgistrationCreateView(CreateView):
    template_name = 'home/auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
