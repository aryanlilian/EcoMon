from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import User, Income, Spending, Profile
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from common.constants import error_messages, help_texts
from PIL import Image
from django.core.files import File


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), help_text=help_texts['email'])
    first_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
    last_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
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
    email = forms.EmailField(widget=forms.EmailInput(), help_text=help_texts['email'])
    first_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
    last_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
    birth_date = forms.DateField(help_text=help_texts['date'])
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

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError(
                error_messages['required'],
                code='first_name_empty'
            )
        if not first_name.isalpha():
            raise ValidationError(
                error_messages['first_name'],
                code='first_name_invalid'
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise ValidationError(
                error_messages['required'],
                code='last_name_empty'
            )
        if not last_name.isalpha():
            raise ValidationError(
                error_messages['last_name'],
                code='last_name_invalid'
            )
        return last_name

class ProfileUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 82}),
        help_text=help_texts['profile_description'],
        required=False
    )

    class Meta:
        model = Profile
        fields = [
            'image',
            'description',
            'currency',
        ]


class PhotoUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), label='')
    
    class Meta:
        model = Profile
        fields = ['image']


class IncomeCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, label='Name',
        help_text=help_texts['obj_name']
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=3,
        label='Amount',
        help_text=help_texts['obj_amount']
    )
    recurrent = forms.BooleanField(required=False, label='Recurrent?')

    class Meta:
        model = Income
        exclude = [
            'user',
            'created_date'
        ]


class SpendingCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        label='Name',
        help_text=help_texts['obj_name']
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=3,
        label='Amount',
        help_text=help_texts['obj_amount']
    )
    recurrent = forms.BooleanField(required=False, label='Recurrent?')

    class Meta:
        model = Spending
        exclude = [
            'user',
            'created_date'
        ]
