from django.urls import path, include

from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('', include('board.urls')),

]