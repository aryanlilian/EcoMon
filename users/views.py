from django.views.generic import CreateView, ListView, DeleteView
from .models import Income, Spending
from .forms import IncomeCreateForm, SpendingCreateForm
from .utils import assembly, recurrent_check
from django.urls import reverse_lazy
from datetime import datetime
from . import constants


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
