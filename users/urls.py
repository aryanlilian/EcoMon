from django.urls import path
from .views import (
    AccountsListView, DashboardView, ProfileView,
    IncomesCreateListView, SpendingsCreateListView, AccountCreateView,
    IncomeUpdateView, SpendingUpdateView, AccountUpdateView,
    IncomeDeleteView, SpendingDeleteView, ArchiveView,
    EmailVerificationView, SendOrVerifyEmailVerificationView
)
from .helpers import (
    incomes_chart_area, incomes_chart_pie, spendings_chart_area,
    spendings_chart_pie,
)

urlpatterns = [
    path('accounts/', AccountsListView.as_view(), name='accounts'),
    path('dashboard/<int:pk>/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dashboard/incomes-chart-area/<int:pk>/', incomes_chart_area, name='incomes-chart-area'),
    path('dashboard/incomes-chart-pie/<int:pk>/', incomes_chart_pie, name='incomes-chart-pie'),
    path('dashboard/spendings-chart-area/<int:pk>/', spendings_chart_area, name='spendings-chart-area'),
    path('dashboard/spendings-chart-pie/<int:pk>/', spendings_chart_pie, name='spendings-chart-pie'),
    path('incomes/new/<int:pk>/', IncomesCreateListView.as_view(), name='incomes'),
    path('spendings/new/<int:pk>/', SpendingsCreateListView.as_view(), name='spendings'),
    path('accounts/new/', AccountCreateView.as_view(), name='accounts-new'),
    path('incomes/update/<int:pk>/', IncomeUpdateView.as_view(), name='update-income'),
    path('spendings/update/<int:pk>/', SpendingUpdateView.as_view(), name='update-spending'),
    path('accounts/update/<int:pk>/', AccountUpdateView.as_view(), name='update-account'),
    path('incomes/delete/<int:pk>/', IncomeDeleteView.as_view(), name='delete-income'),
    path('spendings/delete/<int:pk>/', SpendingDeleteView.as_view(), name='delete-spending'),
    path('archive/', ArchiveView.as_view(), name='archive'),
    path('verification/', EmailVerificationView.as_view(), name='email-verification'),
    path('send/verification/<uidb64>/<token>/', SendOrVerifyEmailVerificationView.as_view(), name='send-or-verify-email-verification'),
]
