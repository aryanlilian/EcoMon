from django.shortcuts import render
from django.views.generic import CreateView
from .forms import NewsletterForm


class IndexFormView(CreateView):
    template_name = 'home/index.html'
    form_class = NewsletterForm

    def form_valid(self, form):
        return super().form_valid(form)
