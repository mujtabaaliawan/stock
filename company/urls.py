from django.urls import path
from company import views


urlpatterns = [
    path('company', views.CompanyList.as_view(), name='company_list'),
    path('company/new', views.CompanyCreate.as_view(), name='company_new'),
    path('company/<int:pk>', views.CompanyUpdate.as_view(), name='company_update'),
]
