from django.urls import path
from category import views


urlpatterns = [
    path('category', views.CategoryList.as_view(), name='category_list'),
    path('category/new', views.CategoryCreate.as_view(), name='category_new'),
    path('category/<int:pk>', views.CategoryUpdate.as_view(), name='category_update'),
    path('enrollment/<int:pk>', views.Enrollment.as_view(), name='enrollment'),
    path('enrollment/update/<int:pk>', views.EnrollmentUpdate.as_view(), name='enrollment_update')

]
