from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from price.test.factories import TraderFactory
import json
from rest_framework.test import RequestsClient


class TestPrice(APITestCase):

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

    def test_post_dataupater(self):

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

    def test_get_latest_prices(self):

        self.test_post_dataupater()

        data = [
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Hino Pak Motor Limited.", "ldcp": 245.5, "open": 228.02, "high": 228.02, "low": 227.1, "current": 227.1, "change": -18.4, "volume": 400.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Honda Atlas Cars (Pak) Ltd.", "ldcp": 150.08, "open": 146.5, "high": 150.15, "low": 146.5, "current": 148.0, "change": -2.08, "volume": 28449.0, "date_time": "2022-12-08 11:59:05"}
        ]

        self.user_login(email=self.trader.user.email, password='trader')
        path = reverse('market_price')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        market_data = json.loads(response.content)

        self.assertEqual(market_data["1"]["category_name"], data[0]["category"])
        self.assertEqual(market_data["1"]["company_name"], data[0]["company"])
        self.assertEqual(market_data["1"]["ldcp"], data[0]["ldcp"])
        self.assertEqual(market_data["1"]["open"], data[0]["open"])
        self.assertEqual(market_data["1"]["high"], data[0]["high"])
        self.assertEqual(market_data["1"]["low"], data[0]["low"])
        self.assertEqual(market_data["1"]["current"], data[0]["current"])
        self.assertEqual(market_data["1"]["change"], data[0]["change"])
        self.assertEqual(market_data["1"]["volume"], data[0]["volume"])
        self.assertEqual(market_data["1"]["date_time"], data[0]["date_time"].replace(' ', 'T'))

        self.assertEqual(market_data["2"]["category_name"], data[1]["category"])
        self.assertEqual(market_data["2"]["company_name"], data[1]["company"])
        self.assertEqual(market_data["2"]["ldcp"], data[1]["ldcp"])
        self.assertEqual(market_data["2"]["open"], data[1]["open"])
        self.assertEqual(market_data["2"]["high"], data[1]["high"])
        self.assertEqual(market_data["2"]["low"], data[1]["low"])
        self.assertEqual(market_data["2"]["current"], data[1]["current"])
        self.assertEqual(market_data["2"]["change"], data[1]["change"])
        self.assertEqual(market_data["2"]["volume"], data[1]["volume"])
        self.assertEqual(market_data["2"]["date_time"], data[1]["date_time"].replace(' ', 'T'))
