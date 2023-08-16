from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsAdminUser]
        if self.request.method == "GET":
            permission_classes = []
        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method == "GET":
            permission_classes = []
        if self.request.method in ["PATCH", "DELETE"]:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
