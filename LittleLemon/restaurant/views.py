from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .models import User, Menu,Booking
from rest_framework.response import Response

# Create your views here
def index(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer(queryset)
    #permission_classes = [permissions.IsAuthenticated]
    def list(self,request):
        return Response ()
    
    #MenuItemView Working
class MenuItemView (generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get(self, request):
        return Response()
    def post(self,request):
        return Response()

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def get(self,request):
        return Response()
    def post(self,request):
        return Response()
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get(self,request):
        return Response()
