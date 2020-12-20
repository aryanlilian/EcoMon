from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import NewsletterForm
from .models import Testimonial


class IndexFormView(CreateView):
    template_name = 'home/index.html'
    form_class = NewsletterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.order_by('-date_added')
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class AboutTemplateView(TemplateView):
    template_name = 'home/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'home/contact.html'
