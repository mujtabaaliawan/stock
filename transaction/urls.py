from django.urls import path
from transaction.views import views


urlpatterns = [
    path('transaction', views.TransactionListCreate.as_view(), name='transaction_list_new'),
]
