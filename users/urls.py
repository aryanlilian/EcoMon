from django.urls import path
from .views import (
    DashboardListView,
    IncomeCreateListView,
    SpendingCreateListView,
    # IncomeDeleteView,
)
from .chart_functions import (
    incomes_chart_area_data,
    incomes_chart_pie_data,
    spendings_chart_area_data,
    spendings_chart_pie_data,
)

urlpatterns = [
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
    path('dashboard/incomes-chart-area/', incomes_chart_area_data,
         name='incomes-chart-area'),
    path('dashboard/incomes-chart-pie/', incomes_chart_pie_data,
         name='incomes-chart-pie'),
    path('dashboard/spendings-chart-area/', spendings_chart_area_data,
         name='spendings-chart-area'),
    path('dashboard/spendings-chart-pie/', spendings_chart_pie_data,
         name='spendings-chart-pie'),
    path('income/', IncomeCreateListView.as_view(), name='income'),
    path('spending/', SpendingCreateListView.as_view(), name='spending'),
    # !!!! Incomplete !!!!
    # path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='delete-income'),
]
