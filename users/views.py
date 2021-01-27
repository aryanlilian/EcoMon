from django.urls import reverse_lazy, reverse
from datetime import datetime
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Income, Spending, User
from django.contrib.auth.mixins import LoginRequiredMixin
from random import randint
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from common.mixins import (
    ObjectCreateListViewMixin, ObjectUpdateViewMixin, ObjectDeleteViewMixin,
    EmailTokenGenerator, IsEmailVerifiedMixin, SendEmailThreadMixin
)
from .models import (
    Income, Spending, Profile,
)
from .forms import (
    UserUpdateForm, ProfileUpdateForm, PhotoUpdateForm,
    IncomeCreateForm, SpendingCreateForm
)
from .utils import (
    assembly, percentages_of_incomes, daily_avg,
    max_amount,
)
from common.constants import (
    template_titles, help_texts, email_activation,
)



class DashboardView(LoginRequiredMixin, View):
    template_name ='users/dashboard.html'

    def get(self, request):
        date = datetime.now()
        incomes = Income.objects.filter(
            user=request.user, created_date__year=date.year, created_date__month=date.month
        )
        spendings = Spending.objects.filter(
            user=request.user, created_date__year=date.year, created_date__month=date.month
        )
        currency = Profile.objects.get(user=self.request.user).currency
        total_incomes, total_spendings = assembly(incomes), assembly(spendings)
        total_savings = total_incomes - total_spendings
        spendings_percent = percentages_of_incomes(total_incomes, total_spendings)
        savings_percent = percentages_of_incomes(total_incomes, total_savings)
        max_income, max_spending = max_amount(incomes), max_amount(spendings)
        context = {
            'title': template_titles['dashboard_title'],
            'incomes': incomes,
            'spendings': spendings,
            'currency': currency,
            'total_incomes': total_incomes,
            'total_spendings': total_spendings,
            'total_savings': total_savings,
            'spendings_percent': spendings_percent ,
            'savings_percent': savings_percent,
            'max_income': max_income,
            'max_spending': max_spending,
        }
        return render(request, self.template_name, context)


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user_update_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_update_form = ProfileUpdateForm(
            request.POST,
            instance=request.user.profile
        )
        photo_update_form = PhotoUpdateForm(
            request.POST, request.FILES,
            instance=request.user.profile
        )
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(
                request,
                'Your profile was updated successful!'
            )
            return redirect('profile')
        if photo_update_form.is_valid():
            photo_update_form.save()
            messages.success(
                request,
                'Your profile picture was updated successful!'
            )
            return redirect('profile')
        context['user_update_form'] = user_update_form
        context['profile_update_form'] = profile_update_form
        context['photo_update_form'] = photo_update_form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        user_update_form = UserUpdateForm(
            instance = self.request.user
        )
        profile_update_form = ProfileUpdateForm(
            instance = self.request.user.profile
        )
        photo_update_form = PhotoUpdateForm(
            instance = self.request.user.profile
        )
        context = {
            'title' : template_titles['profile_title'],
            'user_update_form' : user_update_form,
            'profile_update_form' : profile_update_form,
            'photo_update_form' : photo_update_form,
            'phone_number_help_text' : help_texts['phone_number']
        }
        return context


class IncomesCreateListView(LoginRequiredMixin, ObjectCreateListViewMixin):
    model = Income
    form_class = IncomeCreateForm
    model_name = 'Incomes'
    color = 'primary'


class SpendingsCreateListView(LoginRequiredMixin, ObjectCreateListViewMixin):
    model = Spending
    form_class = SpendingCreateForm
    model_name = 'Spendings'
    color = 'danger'


class IncomeUpdateView(ObjectUpdateViewMixin):
    model = Income
    model_name = 'Incomes'

class SpendingUpdateView(ObjectUpdateViewMixin):
    model = Spending
    model_name = 'Spendings'

class IncomeDeleteView(ObjectDeleteViewMixin):
    model = Income
    success_url = reverse_lazy('incomes')


class SpendingDeleteView(ObjectDeleteViewMixin):
    model = Spending
    success_url = reverse_lazy('spendings')


class ArchiveView(LoginRequiredMixin, View):
    template_name = 'users/archive.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        incomes = Income.objects.filter(user=request.user)
        spendings = Spending.objects.filter(user=request.user)
        total_incomes, total_spendings = assembly(incomes), assembly(spendings)
        context['incomes'] = incomes
        context['spendings'] = spendings
        context['total_incomes'] = total_incomes
        context['total_spendings'] = total_spendings
        context['total_savings'] = total_incomes - total_spendings
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        year = datetime.strptime(request.POST.get('year'), '%Y')
        month = datetime.strptime(request.POST.get('month'), '%m')
        incomes = Income.objects.filter(
            user=request.user, created_date__year=year.year, created_date__month=month.month
        )
        spendings = Spending.objects.filter(
            user=request.user, created_date__year=year.year, created_date__month=month.month
        )
        total_incomes, total_spendings = assembly(incomes), assembly(spendings)
        context['incomes'] = incomes
        context['spendings'] = spendings
        context['total_incomes'] = total_incomes
        context['total_spendings'] = total_spendings
        context['total_savings'] = total_incomes - total_spendings
        context['year'] = year
        context['month'] = month
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
            'currency': Profile.objects.get(user=self.request.user).currency
        }
        return context


class EmailVerificationView(LoginRequiredMixin, IsEmailVerifiedMixin, View):

    def get(self, request, *args, **kwargs):
        domain = get_current_site(request).domain
        token_generator = EmailTokenGenerator()
        uidb64 = urlsafe_base64_encode(force_bytes(request.user.id))
        relatively_url = reverse(
            'send-or-verify-email-verification',
            kwargs={'uidb64' : uidb64, 'token' : token_generator.make_token(request.user)}
        )
        activate_url = 'http://' + domain + relatively_url
        subject = email_activation['subject']
        body = email_activation['body'] + activate_url
        to_email = request.user.email
        email = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [to_email],
        )
        SendEmailThreadMixin(email).start()
        return redirect('dashboard')


class SendOrVerifyEmailVerificationView(LoginRequiredMixin, View):

    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            token_generator = EmailTokenGenerator()
            if not token_generator.check_token(user, token):
                messages.error(request, 'You\'ve already used the activation link, your email is verified!')
                return redirect('dashboard')
            user.email_verified = True
            user.save()
            messages.success(request, 'Your email was verified successfuly!')
        except Exception as e:
            messages.info(request, 'Something went wrong!')
        return redirect('dashboard')
