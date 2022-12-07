from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('token', TokenObtainPairView.as_view(), name='token_new'),
    path('token-refresh', TokenRefreshView.as_view(), name='token_update'),
    path('', include('category.urls')),
    path('', include('company.urls')),
    path('', include('price.urls')),
    path('', include('favourite.urls')),
    path('', include('trader.urls')),
    path('', include('transaction.urls')),
    path('', include('user.urls')),
]
