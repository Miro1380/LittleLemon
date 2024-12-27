#define URL route for index() view
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('user/', views.UserViewSet.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('booking/', views.BookingViewSet.as_view())
]
