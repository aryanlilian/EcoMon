from django.urls import path
from .views import IncomeCreateListView, SpendingCreateListView

urlpatterns = [
    path('income/', IncomeCreateListView.as_view(), name='income'),
    path('spending/', SpendingCreateListView.as_view(), name='spending'),
]
