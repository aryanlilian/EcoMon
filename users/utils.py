from calendar import monthrange
from datetime import datetime


def assembly(obj):
    return round(sum(i.amount for i in obj), 2)


def percentages_of_incomes(incomes, obj_sum):
    return round((obj_sum / incomes) * 100, 2) if incomes > 0 else 0


def days_of_month(year, month):
    return monthrange(year, month)[1]


def daily_avg(obj_sum, days):
    return round(obj_sum / days, 2)


def max_amount(objs=None):
    if objs:
        return max(i.amount for i in objs)


def check_recurrent_or_new(user, objs, model):
    for item in objs:
        date_test = item.created_date.month == 12
        date = datetime(
            item.created_date.year + 1 if date_test else item.created_date.year,
            1 if date_test else item.created_date.month + 1, item.created_date.day,
            item.created_date.hour, item.created_date.minute, item.created_date.second,
            item.created_date.microsecond
        )
        obj,created = model.objects.get_or_create(
            user=user, name=item.name, amount=item.amount,
            created_date=date, category=item.category, recurrent=True
        )


def delete_recurrent_object(user, obj, model):
    date_test = obj.created_date.month == 12
    date = datetime(
        obj.created_date.year + 1 if date_test else obj.created_date.year,
        1 if date_test else obj.created_date.month + 1, obj.created_date.day,
        obj.created_date.hour, obj.created_date.minute, obj.created_date.second,
        obj.created_date.microsecond
    )
    object = model.objects.get(
        user=user, name=obj.name, amount=obj.amount,
        created_date=date, category=obj.category, recurrent=True
    )
    object.delete()
