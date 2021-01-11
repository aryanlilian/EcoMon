from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm
from .models import User, Income, Spending, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserRegistrationForm
    list_display = ['__str__', 'is_superuser', 'is_staff', 'is_active', 'date_joined']

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Phone Number',
            {
                'fields': (
                    'phone_number',
                )
            }
        ),
        (
            'Email Status',
            {
                'fields': (
                    'do_not_marketing_email',
                    'email_verified'
                )
            }
        ),
        (
            'Birth Date',
            {
                'fields': (
                    'birth_date',
                )
            }
        ),
        (
            'Terms & Conditions',
            {
                'fields': (
                    'accept_terms_and_conditions',
                )
            }
        ),
    )

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)

@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)
