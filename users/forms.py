from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User, Income, Spending


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class IncomeCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Name')
    amount = forms.DecimalField(
        max_digits=10, decimal_places=3, label='Amount')
    recurrent = forms.BooleanField(label='Recurrent?')

    class Meta:
        model = Income
        exclude = ['user']


class SpendingCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Name')
    amount = forms.DecimalField(
        max_digits=10, decimal_places=3, label='Amount')
    recurrent = forms.BooleanField(label='Recurrent?')

    class Meta:
        model = Spending
        exclude = ['user']
