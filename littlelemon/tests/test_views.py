from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemsView


class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu
        menu1 = Menu.objects.create(title="Menu 1", price=10.99, inventory=100)
        menu2 = Menu.objects.create(title="Menu 2", price=15.99, inventory=100)
        menu3 = Menu.objects.create(title="Menu 3", price=12.99, inventory=100)

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse("menu-items")
        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
