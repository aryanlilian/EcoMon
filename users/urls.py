from django.urls import path
from .views import (
    DashboardView,
    ProfileView,
    IncomesCreateListView,
    SpendingsCreateListView,
    IncomeDeleteView,
    ArchiveView,
)
from .helpers import (
    incomes_chart_area_data,
    incomes_chart_pie_data,
    spendings_chart_area_data,
    spendings_chart_pie_data,
)

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dashboard/incomes-chart-area/', incomes_chart_area_data, name='incomes-chart-area'),
    path('dashboard/incomes-chart-pie/', incomes_chart_pie_data, name='incomes-chart-pie'),
    path('dashboard/spendings-chart-area/', spendings_chart_area_data, name='spendings-chart-area'),
    path('dashboard/spendings-chart-pie/', spendings_chart_pie_data, name='spendings-chart-pie'),
    path('incomes/', IncomesCreateListView.as_view(), name='incomes'),
    path('spendings/', SpendingsCreateListView.as_view(), name='spendings'),
    # !!!! Incomplete !!!!
    path('income/delete/<int:pk>/', IncomeDeleteView.as_view(), name='delete-income'),
    path('archive', ArchiveView.as_view(), name='archive'),
]
