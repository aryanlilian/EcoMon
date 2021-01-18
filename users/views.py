from django.urls import reverse_lazy
from datetime import datetime
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from . import constants
# from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ObjectCreateListViewMixin
from .models import (
    Income,
    Spending,
    Profile,
)
from .forms import (
    UserUpdateForm,
    ProfileUpdateForm,
    IncomeCreateForm,
    SpendingCreateForm
)
from .utils import (
    assembly,
    percentages_of_incomes,
    daily_avg,
    max_amount,
    recurrent_check,
)


class DashboardView(LoginRequiredMixin, View):
    template_name ='users/dashboard.html'

    def get(self, request):
        date = datetime.now()
        incomes = Income.objects.filter(user=request.user, created_date__year=date.year, created_date__month=date.month)
        spendings = Spending.objects.filter(user=request.user, created_date__year=date.year, created_date__month=date.month)
        currency = Profile.objects.get(user=self.request.user).currency
        total_incomes, total_spendings = assembly(incomes), assembly(spendings)
        total_savings = total_incomes - total_spendings
        spendings_percent = percentages_of_incomes(total_incomes, total_spendings)
        savings_percent = percentages_of_incomes(total_incomes, total_savings)
        max_income, max_spending = max_amount(incomes), max_amount(spendings)
        context = {
            'title': 'Dashboard',
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
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, 'Your profile was updated successful!')
            return redirect('profile')
        context['user_update_form'] = user_update_form
        context['profile_update_form'] = profile_update_form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        user_update_form = UserUpdateForm(instance=self.request.user)
        profile_update_form = ProfileUpdateForm(instance=self.request.user.profile)
        context = {
            'title' : 'Profile',
            'user_update_form' : user_update_form,
            'profile_update_form' : profile_update_form,
        }
        return context


class IncomesCreateListView(LoginRequiredMixin, ObjectCreateListViewMixin):
    form_class = IncomeCreateForm
    model_name = 'Incomes'
    color = 'primary'
    constant = constants.INCOME_OBJECT


class SpendingsCreateListView(LoginRequiredMixin, ObjectCreateListViewMixin):
    form_class = SpendingCreateForm
    model_name = 'Spendings'
    color = 'danger'
    constant = constants.SPENDING_OBJECT

# !!!! Incomplete !!!!
# class IncomeDeleteView(DeleteView):
#     model = Income
#     template_name = 'users/delete.html'
#     success_url = reverse_lazy('income')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object_name'] = 'Income'
#         return context


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
        incomes = Income.objects.filter(user=request.user, created_date__year=year.year, created_date__month=month.month)
        spendings = Spending.objects.filter(user=request.user, created_date__year=year.year, created_date__month=month.month)
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
