"""shops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from stores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', views.shop_list, name="shop-list"),
    path('item/', views.item_list, name="item-list"),
    path('shop/create', views.shop_create, name="shop-create"),
    path('item/create', views.item_create, name="item-create"),
    path('item/update/<int:item_id>/', views.item_update, name="item-update"),     
]
