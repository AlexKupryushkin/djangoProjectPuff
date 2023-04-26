from django.contrib import admin
from django.contrib.auth import login
from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),

    path('sofas/<category_name>', DivansCategoryListView.as_view(), name='divan_'),
    path('list/<int:divan_id>', DivanView.as_view(), name='one_divan'),

    # корзина
    path("add/<int:divan_id>", views.AddDivanView.as_view(), name="add-divan"),
    path("cart/", views.ShowCartView.as_view(), name="show-cart"),

    # регистрация и авторизация
    path('reg/', RegisterUser.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),



]


