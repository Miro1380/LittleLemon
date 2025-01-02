#define URL route for index() view
from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.index, name='index'),
    #path('user/', views.UserViewSet.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    #path('booking/', views.BookingViewSet.as_view())
]
