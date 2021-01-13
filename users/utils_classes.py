from datetime import datetime
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from .models import Profile
from .utils_functions import (
    assembly,
    percentages_of_incomes,
    days_of_month,
    daily_avg,
    max_amount,
    recurrent_check,
)


class ObjectCreatListView(CreateView):
    template_name = 'users/incomes_&_spendings.html'
    form_class = None
    model_name = None
    color = None
    constant = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.constant.objects.filter(user=self.request.user, created_date__year=datetime.now(
        ).year, created_date__month=datetime.now().month)
        recurrent_obj = self.constant.objects.filter(user=self.request.user, recurrent=True,
                                                     created_date__year=datetime.now().year, created_date__month=datetime.now().month)
        if datetime.now().month == 1:
            obj_last_month = self.constant.objects.filter(user=self.request.user, created_date__year=datetime.now(
            ).year - 1, created_date__month=datetime.now().month + 11)
        else:
            obj_last_month = self.constant.objects.filter(user=self.request.user, created_date__year=datetime.now(
            ).year, created_date__month=datetime.now().month - 1)
        total_obj = round(assembly(obj), 2)
        total_obj_last_month = round(assembly(obj_last_month), 2)
        recurrent_check(self.request.user, recurrent_obj, self.constant)
        context['title'] = self.model_name
        context['primary_color'] = self.color
        context['objects'] = obj
        context['total_sum'] = total_obj
        context['currency'] = Profile.objects.get(
            user=self.request.user).currency
        context['total_sum_last_month'] = total_obj_last_month
        context['date'] = datetime.now()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
