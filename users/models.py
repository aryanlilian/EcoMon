from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    birth_date = models.DateField(_('Birth Date'), auto_now_add=False, null=True, blank=True)
    phone_number = PhoneNumberField(_('Phone Number'), null=True, blank=True, unique=True)
    email_verified = models.BooleanField(_('Email Verified'), default=False)
    do_not_marketing_email = models.BooleanField(_('Do not marketing email'), default=False)

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'
