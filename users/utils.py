from calendar import monthrange
from datetime import datetime


def assembly(incomes):
    return sum(i.amount for i in incomes)


def spendings_percentages_of_incomes(incomes, spendings):
    return round((spendings / incomes) * 100, 2) if incomes > 0 else 0


def savings_percentages_of_incomes(incomes, savings):
    return round((savings / incomes) * 100, 2) if incomes > 0 else 0


def days_of_month(year, month):
    return monthrange(year, month)[1]


def daily_avg_incomes(incomes, days):
    return round(incomes / days, 2)


def daily_avg_spendings(spendings, days):
    return round(spendings / days, 2)


def daily_avg_savings(savings, days):
    return round(savings / days, 2)


def max_value(objects):
    max_amount = 0
    for i in objects:
        if i.amount > max_amount:
            max_amount = i.amount
    return max_amount
