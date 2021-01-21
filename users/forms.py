from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import User, Income, Spending, Profile
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), help_text='Enter a help text ex: name@example.com')
    first_name = forms.CharField(widget=forms.TextInput(), help_text='Enter just letters')
    last_name = forms.CharField(widget=forms.TextInput())
    marketing_email = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    accept_terms_and_conditions = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'marketing_email',
            'accept_terms_and_conditions'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    birth_date = forms.DateField()
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'birth_date',
            'phone_number',
        ]

    error_messages = {
        'first_name' : _('First name can contain only letters'),
        'last_name' : _('Last name can contain only letters')
    }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError(
                self.error_messages['first_name'],
                code='first_name_invalid'
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError(
                self.error_messages['last_name'],
                code='last_name_invalid'
            )
        return last_name

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 82}))

    class Meta:
        model = Profile
        fields = [
            'image',
            'description',
            'currency',
        ]


class IncomeCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Name', help_text='Enter letters, numbers or special characters')
    amount = forms.DecimalField(max_digits=10, decimal_places=3, label='Amount', help_text='Enter a number with maxim 10 digits and 3 decimals')
    recurrent = forms.BooleanField(required=False, label='Recurrent?')

    class Meta:
        model = Income
        exclude = [
            'user',
            'created_date'
        ]


class SpendingCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Name', help_text='Enter letters, numbers or special characters')
    amount = forms.DecimalField(
        max_digits=10, decimal_places=3, label='Amount', help_text='Enter a number with maxim 10 digits and 3 decimals')
    recurrent = forms.BooleanField(required=False, label='Recurrent?')

    class Meta:
        model = Spending
        exclude = [
            'user',
            'created_date'
        ]
