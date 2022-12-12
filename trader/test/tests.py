from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from trader.test.factories import TraderFactory
import json


class TestTrader(APITestCase):

    def user_login(self, email, password):
        token_data = {
            'email': email,
            'password': password
        }
        token_path = reverse('token_new')
        access_token = self.client.post \
            (token_path, json.dumps(token_data), content_type='application/json').data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.login(email=email, password=password)
        self.assertEqual(response, True)

    def test_create_trader(self):
        test_data = {
            "user": {
                "email": "john@gmail.com",
                "first_name": "John",
                "last_name": "Smith",
                "password": "john",
                "role": "trader",
            },
            "mobile_number": "03004567823"
        }
        path = reverse('trader_new')

        self.trader = TraderFactory.create()
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_trader(self):

        test_data = {
            "mobile_number": "03004567823"
        }
        self.trader = TraderFactory.create()

        path = reverse('trader_list')
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.get(path)
        self.assertEqual(response.data[0].get('mobile_number'), self.trader.mobile_number)

        path = reverse('trader_update', kwargs={'pk': self.trader.id})
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.patch(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('mobile_number'), test_data['mobile_number'])

    def test_get_trader_list(self):

        path = reverse('trader_list')

        self.trader = TraderFactory.create()
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['user']['first_name'], self.trader.user.first_name)
        self.assertEqual(response.data[0]['user']['last_name'], self.trader.user.last_name)
        self.assertEqual(response.data[0]['user']['email'], self.trader.user.email)
        self.assertEqual(response.data[0]['user']['role'], self.trader.user.role)
        self.assertEqual(response.data[0]['mobile_number'], self.trader.mobile_number)


