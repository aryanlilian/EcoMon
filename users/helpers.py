from .models import Income, Spending, Account, Profile
from common.utils import assembly, total_currency_converter
from datetime import datetime
from django.http import JsonResponse


# def chart_area(request, pk=None):
#     data, date_distance, checks = [], -1, 12
#     account = Account.objects.get(id=pk) if pk else None
#     accounts = Account.objects.filter(user=request.user) if not pk else None
#     profile_currency = Profile.objects.get(user=request.user).currency if not pk else None
#     object = Income if '/users/dashboard/incomes-chart-area/' in request.get_full_path() else Spending
#     first_object = object.objects.filter(user=request.user, account=account).first() if account else object.objects.filter(user=request.user).first()
#     last_object = object.objects.filter(user=request.user, account=account).last() if account else object.objects.filter(user=request.user).last()
#     if first_object and last_object:
#         date_distance = (last_object.created_date - first_object.created_date).days
#     if  1 <= date_distance <= 365:
#         year, month = first_object.created_date.year, first_object.created_date.month
#         while checks:
#             date = datetime(year, month, 1)
#             if month == 12:
#                 if pk:
#                     objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
#                     data.append({date.strftime('%b'): assembly(objects)})
#                 else:
#                     objects = total_currency_converter(request.user, object, accounts, profile_currency, year, month)
#                     data.append({date.strftime('%b'): objects})
#                 month = 1
#                 year += 1
#             else:
#                 if pk:
#                     objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
#                     data.append({date.strftime('%b'): assembly(objects)})
#                 else:
#                     objects = total_currency_converter(request.user, object, accounts, profile_currency, year, month)
#                     data.append({date.strftime('%b'): objects})
#                 month += 1
#             checks -= 1
#     elif date_distance > 0:
#         year, month = last_object.created_date.year - 1, last_object.created_date.month + 1
#         while checks:
#             date = datetime(year, month, 1)
#             if month == 12:
#                 if pk:
#                     objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
#                     data.append({date.strftime('%b'): assembly(objects)})
#                 else:
#                     objects = total_currency_converter(request.user, object, accounts, profile_currency, year, month)
#                     data.append({date.strftime('%b'): objects})
#                 month = 1
#                 year += 1
#             else:
#                 if pk:
#                     objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
#                     data.append({date.strftime('%b'): assembly(objects)})
#                 else:
#                     objects = total_currency_converter(request.user, object, accounts, profile_currency, year, month)
#                     data.append({date.strftime('%b'): objects})
#                 month += 1
#             checks -= 1
#     elif date_distance == 0:
#         year, month = first_object.created_date.year, first_object.created_date.month
#         while checks:
#             date = datetime(year, month, 1)
#             if month == 12:
#                 if pk:
#                     objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
#                     data.append({date.strftime('%b'): assembly(objects)})
#                 else:
#                     objects = total_currency_converter(request.user, object, accounts, profile_currency, year, month)
#                     data.append({date.strftime('%b'): objects})
#                 month = 1
#                 year += 1
#             else:
#                 if pk:
#                     objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
#                     data.append({date.strftime('%b'): assembly(objects)})
#                 else:
#                     objects = total_currency_converter(request.user, object, accounts, profile_currency, year, month)
#                     data.append({date.strftime('%b'): objects})
#                 month += 1
#             checks -= 1
#     return JsonResponse(data, safe=False)
#
#
# def chart_pie(request, pk=None):
#     date = datetime.now()
#     account = Account.objects.get(id=pk) if pk else None
#     accounts = Account.objects.filter(user=request.user) if not pk else None
#     currency = Profile.objects.get(user=request.user).currency if not pk else None
#     object = Income if '/users/dashboard/incomes-chart-pie/' in request.get_full_path() else Spending
#     if account:
#         objects = object.objects.filter(user=request.user, account=account, created_date__year=date.year, created_date__month=date.month)
#         total_objects = assembly(objects)
#     else:
#         objects = object.objects.filter(user=request.user, created_date__year=date.year, created_date__month=date.month)
#         total_objects = total_currency_converter(request.user, object, accounts, currency, date.year, date.month)
#     data = []
#     categories = ['Salary', 'Awards', 'Grants', 'Sale', 'Dividents', 'Rental', 'Refunds', 'Coupons', 'Lottery', 'Capital', 'Investments', 'Gift', 'Others'] if object is Income else ['Utilities', 'Rent', 'Invoices', 'Shopping', 'Food', 'Education', 'Fun', 'Investment', 'Others']
#     for category in categories:
#         if account:
#             category_objects = object.objects.filter(user=request.user, account=account, created_date__year=dateyear, created_date__month=date.month, category=category)
#             total_category_objects = assembly(category_objects)
#         else:
#             category_objects = object.objects.filter(user=request.user, created_date__year=date.year, created_date__month=date.month, category=category)
#             total_category_objects = total_currency_converter(request.user, object, accounts, currency, date.year, date.month)
#             print(f'Object: {object}, total objects {total_objects},  total category objects {total_category_objects}')
#         if total_objects and total_category_objects:
#             data.append({category: round((total_category_objects / total_objects) * 100, 2)})
#     return JsonResponse(data, safe=False)


def chart_area(request, pk=None):
    data, date_distance, checks = [], -1, 12
    account = Account.objects.get(id=pk) if pk else None
    object = Income if '/users/dashboard/incomes-chart-area/' in request.get_full_path() else Spending
    first_object = object.objects.filter(user=request.user, account=account).first() if account else object.objects.filter(user=request.user).first()
    last_object = object.objects.filter(user=request.user, account=account).last() if account else object.objects.filter(user=request.user).last()
    if first_object and last_object:
        date_distance = (last_object.created_date - first_object.created_date).days
    if  1 <= date_distance <= 365:
        year, month = first_object.created_date.year, first_object.created_date.month
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
                data.append({date.strftime('%b'): assembly(objects)})
                month = 1
                year += 1
            else:
                objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
                data.append({date.strftime('%b'): assembly(objects)})
                month += 1
            checks -= 1
    elif date_distance > 0:
        year, month = last_object.created_date.year - 1, last_object.created_date.month + 1
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
                data.append({date.strftime('%b'): assembly(objects)})
                month = 1
                year += 1
            else:
                objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
                data.append({date.strftime('%b'): assembly(objects)})
                month += 1
            checks -= 1
    elif date_distance == 0:
        year, month = first_object.created_date.year, first_object.created_date.month
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
                data.append({date.strftime('%b'): assembly(objects)})
                month = 1
                year += 1
            else:
                objects = object.objects.filter(user=request.user, account=account, created_date__year=year, created_date__month=month)
                data.append({date.strftime('%b'): assembly(objects)})
                month += 1
            checks -= 1
    return JsonResponse(data, safe=False)


def chart_pie(request, pk=None):
    account = Account.objects.get(id=pk) if pk else None
    object = Income if '/users/dashboard/incomes-chart-pie/' in request.get_full_path() else Spending
    objects = object.objects.filter(user=request.user, account=account, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
    total_objects = assembly(objects)
    data = []
    categories = ['Salary', 'Awards', 'Grants', 'Sale', 'Dividents', 'Rental', 'Refunds', 'Coupons', 'Lottery', 'Capital', 'Investments', 'Gift', 'Others'] if object is Income else ['Utilities', 'Rent', 'Invoices', 'Shopping', 'Food', 'Education', 'Fun', 'Investment', 'Others']
    for category in categories:
        category_objects = object.objects.filter(user=request.user, account=account, created_date__year=datetime.now().year, created_date__month=datetime.now().month, category=category)
        total_category_objects = assembly(category_objects)
        if total_objects and total_category_objects:
            data.append({category: round((total_category_objects / total_objects) * 100, 2)})
    return JsonResponse(data, safe=False)
