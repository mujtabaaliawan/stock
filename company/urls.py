from django.urls import path
from company import views


urlpatterns = [
    path('company', views.CompanyList.as_view(), name='company_list'),
]
