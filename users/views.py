from django.urls import reverse_lazy
from datetime import datetime
from . import constants
from django.views import View
from django.shortcuts import render
from django.views.generic import CreateView  #, DeleteView
from .forms import IncomeCreateForm, SpendingCreateForm
from .models import (
    Income,
    Spending,
    Profile,
)
from .utils_functions import (
    assembly,
    percentages_of_incomes,
    days_of_month,
    daily_avg,
    max_amount,
    recurrent_check,
)


class DashboardListView(View):

    def get(self, request):
        number_of_days = days_of_month(
            datetime.now().year, datetime.now().month)
        incomes = Income.objects.filter(
            user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        spendings = Spending.objects.filter(
            user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        context = {
            'title': 'Dashboard',
            'spendings': spendings,
            'incomes': incomes,
            'currency' : Profile.objects.get(user=self.request.user).currency,
            'max_income' : max_amount(incomes),
            'max_spending': max_amount(spendings),
            'total_incomes': round(assembly(incomes), 2),
            'total_spendings': round(assembly(spendings), 2),
            'total_savings': round(assembly(incomes) - assembly(spendings), 2),
            'spendings_percent': percentages_of_incomes(assembly(incomes), assembly(spendings)),
            'savings_percent': percentages_of_incomes(assembly(incomes), round(assembly(incomes) - assembly(spendings), 2)),
            'avg_incomes': daily_avg(assembly(incomes), number_of_days),
            'avg_spendings': daily_avg(assembly(spendings), number_of_days),
            'avg_savings': daily_avg(assembly(incomes) - assembly(spendings), number_of_days),
        }
        return render(request, 'users/dashboard.html', context)


class IncomeCreateListView(CreateView):
    template_name = 'users/incomes_&_spendings.html'
    form_class = IncomeCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        incomes = Income.objects.filter(
            user=self.request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        recurrent_incomes = Income.objects.filter(
            user=self.request.user, recurrent=True, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        if datetime.now().month == 1:
            incomes_last_month = Income.objects.filter(
                user=self.request.user, created_date__year=datetime.now().year - 1, created_date__month=datetime.now().month + 11)
        else:
            incomes_last_month = Income.objects.filter(
                user=self.request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month - 1)
        total_incomes = round(assembly(incomes), 2)
        total_incomes_last_month = round(assembly(incomes_last_month), 2)
        recurrent_check(self.request.user, recurrent_incomes,
                        constants.INCOME_OBJECT)
        context['title'] = 'Incomes'
        context['primary_color'] = 'primary'
        context['objects'] = incomes
        context['total_sum'] = total_incomes
        context['currency'] = Profile.objects.get(user=self.request.user).currency
        context['total_sum_last_month'] = total_incomes_last_month
        context['date'] = datetime.now()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SpendingCreateListView(CreateView):
    template_name = 'users/incomes_&_spendings.html'
    form_class = SpendingCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spendings = Spending.objects.filter(
            user=self.request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        recurrent_spendings = Spending.objects.filter(
            user=self.request.user, recurrent=True, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        if datetime.now().month == 1:
            spendings_last_month = Spending.objects.filter(
                user=self.request.user, created_date__year=datetime.now().year - 1, created_date__month=datetime.now().month + 11)
        else:
            spendings_last_month = Spending.objects.filter(
                user=self.request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month - 1)
        total_spendings = round(assembly(spendings), 2)
        total_spendings_last_month = round(
            assembly(spendings_last_month), 2)
        recurrent_check(self.request.user, recurrent_spendings,
                        constants.SPENDING_OBJECT)
        context['title'] = 'Spendings'
        context['primary_color'] = 'danger'
        context['objects'] = spendings
        context['total_sum'] = total_spendings
        context['currency'] = Profile.objects.get(user=self.request.user).currency
        context['total_sum_last_month'] = total_spendings_last_month
        context['date'] = datetime.now()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# !!!! Incomplete !!!!
# class IncomeDeleteView(DeleteView):
#     model = Income
#     template_name = 'users/delete.html'
#     success_url = reverse_lazy('income')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object_name'] = 'Income'
#         return context
