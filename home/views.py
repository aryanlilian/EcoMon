from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.views import View
from .forms import NewsletterForm
from .models import Newsletter, Testimonial
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


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
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.order_by(
            '-created_date')[:9]
        return context


class AboutTemplateView(TemplateView):
    template_name = 'home/about.html'


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
        success_message, error_message = False, False
        print("Email", from_email)
        try:
            send_mail(
                subject,
                message + '\nsender: ' + from_email,
                settings.EMAIL_HOST_USER,
                ['ecomon.services@gmail.com'],
                fail_silently=False
            )
            success_message = 'We\'ve received your email, you\'ll hear from us very soon!'
        except:
            error_message = 'Something didn\'t work, please try later!'
        context['success_message'] = success_message
        context['error_message'] = error_message
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        return context




class UserResgistrationCreateView(CreateView):
    template_name = 'home/auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
