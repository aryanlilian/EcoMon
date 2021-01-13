from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import NewsletterForm
from .models import Testimonial
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy


class IndexFormView(CreateView):
    template_name = 'home/index.html'
    form_class = NewsletterForm

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
