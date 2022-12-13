from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from transaction.test.factories import TraderFactory
import json
from rest_framework.test import RequestsClient


class TestTransaction(APITestCase):

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

    def test_post_dataupdater(self):

        path = "http://127.0.0.1:8000/handler"
        data = [
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Hino Pak Motor Limited.", "ldcp": 245.5, "open": 228.02, "high": 228.02, "low": 227.1, "current": 227.1, "change": -18.4, "volume": 400.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Honda Atlas Cars (Pak) Ltd.", "ldcp": 150.08, "open": 146.5, "high": 150.15, "low": 146.5, "current": 148.0, "change": -2.08, "volume": 28449.0, "date_time": "2022-12-08 11:59:05"}
        ]
        self.trader = TraderFactory.create()
        self.user_login(email=self.trader.user.email, password='trader')

        client = RequestsClient()
        client.headers.update({"Secret-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYXJrZXQiOiJzdG9jayIsIm5hbWUiOiJqYW5nb19yYW5nbyIsImNpdHkiOiJrYXJhY2hpIiwiaWF0IjoxNTE2MjM5MDIyfQ.-9ijMMtccWA_0NhGfDIPsJWYUYOJuKtE9P7U6-iovDI"})
        response = client.post(path, json=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_transaction(self):

        self.test_post_dataupdater()

        self.user_login(email=self.trader.user.email, password='trader')
        path = reverse('market_price')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        market_data = json.loads(response.content)
        price_id = market_data[0]["id"]

        test_data = {
            "nature": "purchase",
            "volume_transacted": 100.0,
            "price_id": price_id,
            "trader_id": self.trader.id
        }

        path = reverse("transaction_list_new")

        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        test_data = {
            "nature": "purchase",
            "volume_transacted": 100.0,
            "price_id": price_id,
            "trader_id": self.trader.id
        }

        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        test_data = {
            "nature": "sale",
            "volume_transacted": 50.0,
            "price_id": price_id,
            "trader_id": self.trader.id
        }

        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        test_data = {
            "nature": "sale",
            "volume_transacted": 200.0,
            "price_id": price_id,
            "trader_id": self.trader.id
        }

        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        test_data = {
            "nature": "sale",
            "volume_transacted": 150.0,
            "price_id": price_id,
            "trader_id": self.trader.id
        }

        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
