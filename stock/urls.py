from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include('category.urls')),
    path('', include('company.urls')),
    path('', include('price.urls')),
    path('', include('favourite.urls')),
    path('', include('trader.urls')),
    path('', include('transaction.urls')),
    path('', include('user.urls')),
]
