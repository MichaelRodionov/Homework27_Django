from django.contrib import admin
from django.urls import path

from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.check_response),
    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('ad/', views.AdvertisementView.as_view()),
    path('ad/<int:pk>/', views.AdvertisementDetailView.as_view()),
]
