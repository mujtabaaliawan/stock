from django.urls import path
from company.views import views

urlpatterns = [
    path('company', views.CompanyList.as_view(), name='company_list'),
]
