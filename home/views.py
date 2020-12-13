from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import NewsletterForm


class IndexFormView(CreateView):
    template_name = 'home/index.html'
    form_class = NewsletterForm

    def form_valid(self, form):
        return super().form_valid(form)


class AboutTemplateView(TemplateView):
    template_name = 'home/about.html'

class ContactTemplateView(TemplateView):
	template_name = 'home/contact.html'