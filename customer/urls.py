from django.urls import path
from .views import index, about, order, Menu, MenuSearch
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('order/', order.as_view(), name='order'),
	path('menu/', Menu.as_view(), name='menu'),
	path('menu/search/', MenuSearch.as_view(), name='menu-search'),
]