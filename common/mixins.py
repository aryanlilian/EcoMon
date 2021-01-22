from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Profile
from users.utils import (
    assembly, percentages_of_incomes, days_of_month,
    daily_avg, max_amount, recurrent_check,
)


class ObjectCreateListViewMixin(CreateView):
    model = None
    form_class = None
    model_name = None
    color = None
    template_name = 'users/incomes_&_spendings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.now()
        obj = self.model.objects.filter(
            user=self.request.user,
            created_date__year=date.year,
            created_date__month=date.month
        )
        recurrent_obj = self.model.objects.filter(
            user=self.request.user, recurrent=True,
            created_date__year=date.year,
            created_date__month=date.month
        )
        currency = Profile.objects.get(user=self.request.user).currency
        if date.month == 1:
            obj_last_month = self.model.objects.filter(
                user=self.request.user,
                created_date__year=date.year - 1,
                created_date__month=date.month + 11
            )
        else:
            obj_last_month = self.model.objects.filter(
                user=self.request.user,
                created_date__year=date.year,
                created_date__month=date.month - 1
            )
        total_obj = assembly(obj)
        total_obj_last_month = assembly(obj_last_month)
        recurrent_check(self.request.user, recurrent_obj, self.model)
        context['title'] = self.model_name
        context['color'] = self.color
        context['objects'] = obj
        context['total_sum'] = total_obj
        context['currency'] = currency
        context['total_sum_last_month'] = total_obj_last_month
        context['date'] = date
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ObjectUpdateViewMixin(LoginRequiredMixin, UpdateView):
    model = None
    template_name = 'users/update_incomes_and_spendings'
    fields = ['name', 'amount', 'category', 'recurrent']


    def form_valid(self, form):
        form.instance.self.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)


class ObjectDeleteViewMixin(LoginRequiredMixin, DeleteView):
    model = None
    template_name = 'users/incomes_&_spendings.html'
    success_url = None

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)


class IsAuthenticatedMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class IsSuperuserOrStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.is_staff:
            return redirect('blog')
        return super().dispatch(request, *args, **kwargs)
