from django.urls import reverse_lazy
from datetime import datetime
from django.views import View
from django.shortcuts import render
from . import constants
# from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ObjectCreateListViewMixin
from .forms import IncomeCreateForm, SpendingCreateForm
from .models import (
    Income,
    Spending,
    Profile,
)
from .utils_functions import (
    assembly,
    percentages_of_incomes,
    daily_avg,
    max_amount,
    recurrent_check,
)


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        incomes = Income.objects.filter(user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        spendings = Spending.objects.filter(user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        context = {
            'title': 'Dashboard',
            'spendings': spendings,
            'incomes': incomes,
            'currency': Profile.objects.get(user=self.request.user).currency,
            'max_income': max_amount(incomes),
            'max_spending': max_amount(spendings),
            'total_incomes': round(assembly(incomes), 2),
            'total_spendings': round(assembly(spendings), 2),
            'total_savings': round(assembly(incomes) - assembly(spendings), 2),
            'spendings_percent': percentages_of_incomes(assembly(incomes), assembly(spendings)),
            'savings_percent': percentages_of_incomes(assembly(incomes), round(assembly(incomes) - assembly(spendings), 2)),
        }
        return render(request, 'users/dashboard.html', context)


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
        context['incomes'] = incomes
        context['spendings'] = spendings
        context['total_incomes'] = round(assembly(incomes), 2)
        context['total_spendings'] = round(assembly(spendings), 2)
        context['total_savings'] = round(assembly(incomes) - assembly(spendings), 2)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        year = datetime.strptime(request.POST.get('year'), '%Y')
        month = datetime.strptime(request.POST.get('month'), '%m')
        incomes = Income.objects.filter(user=request.user, created_date__year=year.year, created_date__month=month.month)
        spendings = Spending.objects.filter(user=request.user, created_date__year=year.year, created_date__month=month.month)
        context['incomes'] = incomes
        context['spendings'] = spendings
        context['total_incomes'] = round(assembly(incomes), 2)
        context['total_spendings'] = round(assembly(spendings), 2)
        context['total_savings'] = round(assembly(incomes) - assembly(spendings), 2)
        context['year'] = year
        context['month'] = month
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
            'currency': Profile.objects.get(user=self.request.user).currency
        }
        return context
