from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.utils import timezone

class User(AbstractUser):

    birth_date = models.DateField(
        _('Birth Date'), auto_now_add=False, null=True, blank=True)
    phone_number = PhoneNumberField(
        _('Phone Number'), null=True, blank=True, unique=True)
    email_verified = models.BooleanField(_('Email Verified'), default=False)
    do_not_marketing_email = models.BooleanField(
        _('Do not marketing email'), default=False)

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'


class Income(models.Model):

    class IncomeCategory(models.TextChoices):
        SALARY = 'SLRY', _('Salary')
        PROFIT = 'PRFT', _('Profit')
        INTEREST = 'INTR', _('Interest')
        DIVIDENT = 'DVDT', _('Divident')
        RENTAL = 'RNTL', _('Rental')
        CAPITAL = 'CPTL', _('Capital')
        ROYALTY = 'RYLT', _('Royalty')
        GIFT = 'GIFT', _('Gift')
        OTHERS = 'OTHR', _('Others')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=50)
    amount = models.DecimalField(_('Amount'), max_digits=10, decimal_places=3)
    category = models.CharField(_('Category'), max_length=4,
                                choices=IncomeCategory.choices, default=IncomeCategory.SALARY)
    recurrent = models.BooleanField(_('Recurrent Income'), default=False)
    created_date = models.DateTimeField(
        _('Created Date/Time'), default=timezone.now)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'

    def get_absolute_url(self):
        return reverse('income')

class Spending(models.Model):

    class SpendingCategory(models.TextChoices):
        UTILITIES = 'UTLT', _('Utilities')
        RENT = 'RENT', _('Rent')
        INVOICES = 'INVC', _('Invoices')
        SHOPPING = 'SHPG', _('Shopping')
        FOOD = 'FOOD', _('Food')
        EDUCATION = 'EDCN', _('Education')
        FUN = 'FUN', _('Fun')
        INSETMENT = 'INVT', _('Investment')
        OTHERS = 'OTRS', _('Others')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=50)
    amount = models.DecimalField(
        _('Amount'), max_digits=10, decimal_places=3)
    category = models.CharField(_('Category'), max_length=4,
                                choices=SpendingCategory.choices, default=SpendingCategory.UTILITIES)
    recurrent = models.BooleanField(_('Recurrent Spending'), default=False)
    created_date = models.DateTimeField(
        _('Created Date/Time'), default=timezone.now)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'

    def get_absolute_url(self):
        return reverse('spending')

class Profile(models.Model):

    class Currency(models.TextChoices):
        AED = 'AED', _('AED')
        AUD = 'AUD', _('AUD')
        BRL = 'BRL', _('BRL')
        CAD = 'CAD', _('CAD')
        CHF = 'CHF', _('CHF')
        CLP = 'CLP', _('CLP')
        CNY = 'CNY', _('CNY')
        COP = 'COP', _('COP')
        CZK = 'CZK', _('CZK')
        DKK = 'DKK', _('DKK')
        EUR = 'EUR', _('EUR')
        GBP = 'GBP', _('GBP')
        HKD = 'HKD', _('HKD')
        HUF = 'HUF', _('HUF')
        IDR = 'IDR', _('IDR')
        ILS = 'ILS', _('ILS')
        INR = 'INR', _('INR')
        JPY = 'JPY', _('JPY')
        KRW = 'KRW', _('KRW')
        MDL = 'MDL', _('MDL')
        MXN = 'MXN', _('MXN')
        MYR = 'MYR', _('MYR')
        NOK = 'NOK', _('NOK')
        NZD = 'NZD', _('NZD')
        PHP = 'PHP', _('PHP')
        PLN = 'PLN', _('PLN')
        RON = 'RON', _('RON')
        RUB = 'RUB', _('RUB')
        SAR = 'SAR', _('SAR')
        SEK = 'SEK', _('SEK')
        SGD = 'SGD', _('SGD')
        THB = 'THB', _('THB')
        TRY = 'TRY', _('TRY')
        TWD = 'TWD', _('TWD')
        USD = 'USD', _('USD')
        ZAR = 'ZAR', _('ZAR')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        _('Avatar'), default='default.jpg', upload_to='profile_pics')
    currency = models.CharField(_('Currency'),
                                max_length=3, choices=Currency.choices, default=Currency.USD)
    created_date = models.DateTimeField(
        _('Created Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
