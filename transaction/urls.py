from django.urls import path
from transaction import views


urlpatterns = [
    path('transaction', views.TransactionList.as_view(), name='transaction_list'),
    path('transaction/new', views.TransactionCreate.as_view(), name='transaction_new'),
]
