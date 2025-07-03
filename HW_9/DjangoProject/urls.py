"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from store.views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/edit_price', views.product_list, name='product_list'),  # Список товаров route
    path('', base_view, name='home'),  # перенаправляет на главную страницу
    path('products/', views.product_list, name='product_list'),  # Список товаров route
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Объявляем URL
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),  # Редактирование товара
    path('add/', views.add_product, name='add'),  # Добавление товара
    path('add_category/', views.add_category, name='add_category'), # Добавление категории
]
