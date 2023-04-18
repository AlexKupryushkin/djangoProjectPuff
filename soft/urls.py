from django.contrib import admin
from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('sofas/<category_name>', DivansCategoryListView.as_view(), name='divan_'),
    # path('list1/', Divan2ListView.as_view(), name='divan1'),

    path('list/<int:divan_id>', DivanView.as_view(), name='one_divan'),

    path("add/<int:divan_id>", views.AddDivanView.as_view(), name="add-divan"),
    # path("add1/", adddivan, name="add1-divan"),
    path("cart/", views.ShowCartView.as_view(), name="show-cart"),


    path('reg/', RegisterUser.as_view(), name='reg'),


]


