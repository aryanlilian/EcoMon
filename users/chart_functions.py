from .models import Income, Spending
from .utils_functions import assembly
from datetime import datetime
from django.http import JsonResponse


def incomes_chart_area_data(request):
    incomes_data = []
    first_income = Income.objects.filter(user=request.user).first()
    last_income = Income.objects.filter(user=request.user).last()
    date_distance = last_income.created_date - first_income.created_date
    if date_distance.days <= 365:
        year, month, checks = first_income.created_date.year, first_income.created_date.month, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                incomes = Income.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append(
                    {date.strftime('%b'): assembly(incomes)})
                month = 1
                year += 1
            else:
                incomes = Income.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append(
                    {date.strftime('%b'): assembly(incomes)})
                month += 1
            checks -= 1
    else:
        year, month, checks = last_income.created_date.year - \
            1, last_income.created_date.month + 1, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                incomes = Income.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append(
                    {date.strftime('%b'): assembly(incomes)})
                month = 1
                year += 1
            else:
                incomes = Income.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append(
                    {date.strftime('%b'): assembly(incomes)})
                month += 1
            checks -= 1
    return JsonResponse(incomes_data, safe=False)


def spendings_chart_area_data(request):
    spendings_data = []
    first_spending = Spending.objects.filter(user=request.user).first()
    last_spending = Spending.objects.filter(user=request.user).last()
    date_distance = last_spending.created_date - first_spending.created_date
    if date_distance.days <= 365:
        year, month, checks = first_spending.created_date.year, first_spending.created_date.month, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                spendings = Spending.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append(
                    {date.strftime('%b'): assembly(spendings)})
                month = 1
                year += 1
            else:
                spendings = Spending.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append(
                    {date.strftime('%b'): assembly(spendings)})
                month += 1
            checks -= 1
    else:
        year, month, checks = last_spending.created_date.year - \
            1, last_spending.created_date.month + 1, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                spendings = Spending.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append(
                    {date.strftime('%b'): assembly(spendings)})
                month = 1
                year += 1
            else:
                spendings = Spending.objects.filter(
                    user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append(
                    {date.strftime('%b'): assembly(spendings)})
                month += 1
            checks -= 1
    return JsonResponse(spendings_data, safe=False)


def incomes_chart_pie_data(request):
    incomes = Income.objects.filter(
        user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
    incomes_data, categories = [], ['Salary', 'Awards', 'Grants', 'Sale', 'Dividents',
                                    'Rental', 'Refunds', 'Coupons', 'Lottery', 'Capital', 'Investments', 'Gift', 'Others']
    for category in categories:
        category_incomes = Income.objects.filter(user=request.user, created_date__year=datetime.now(
        ).year, created_date__month=datetime.now().month, category=category)
        incomes_data.append(
            {category: round((round(assembly(category_incomes)) / round(assembly(incomes))) * 100, 2)})
    return JsonResponse(incomes_data, safe=False)


def spendings_chart_pie_data(request):
    spendings = Spending.objects.filter(
        user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
    spendings_data, categories = [], ['Utilities', 'Rent', 'Invoices',
                                      'Shopping', 'Food', 'Education', 'Fun', 'Investment', 'Others']
    for category in categories:
        category_spendings = Spending.objects.filter(user=request.user, created_date__year=datetime.now(
        ).year, created_date__month=datetime.now().month, category=category)
        spendings_data.append(
            {category: round((round(assembly(category_spendings)) / round(assembly(spendings))) * 100, 2)})
    return JsonResponse(spendings_data, safe=False)
