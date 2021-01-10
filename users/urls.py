from django.urls import path
from .views import IncomeCreateListView, SpendingCreateListView, IncomeDeleteView

urlpatterns = [
    path('income/', IncomeCreateListView.as_view(), name='income'),
    path('spending/', SpendingCreateListView.as_view(), name='spending'),
    # !!!! Incomplete !!!!
    # path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='delete-income'),
]
