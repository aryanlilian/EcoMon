from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your email'}), label='')

    class Meta:
        model = Newsletter
        exclude = ['subscribed_date']
