from calendar import monthrange
from datetime import datetime
# from .models import Income, Spending


def assembly(obj):
    return sum(i.amount for i in obj)


def percentages_of_incomes(incomes, obj_sum):
    return round((obj_sum / incomes) * 100, 2) if incomes > 0 else 0


def days_of_month(year, month):
    return monthrange(year, month)[1]


def daily_avg(obj_sum, days):
    return round(obj_sum / days, 2)


def max_amount(objs):
    return max(i.amount for i in objs)


def recurrent_check(user, objs, obj):
    for item in objs:
        if item.created_date.month == 12:
            date = datetime(item.created_date.year + 1, 1, item.created_date.day,
                            item.created_date.hour, item.created_date.minute, item.created_date.second)
        else:
            date = datetime(item.created_date.year, item.created_date.month + 1, item.created_date.day,
                            item.created_date.hour, item.created_date.minute, item.created_date.second)
        try:
            obj.objects.get(
                user=user, created_date=date)
        except:
            obj.objects.create(user=user, name=item.name, amount=item.amount,
                               created_date=date, category=item.category, recurrent=True)
