from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from company.factories import TraderFactory
import json
from rest_framework.test import RequestsClient


class TestCompany(APITestCase):

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
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Honda Atlas Cars (Pak) Ltd.", "ldcp": 150.08, "open": 146.5, "high": 150.15, "low": 146.5, "current": 148.0, "change": -2.08, "volume": 28449.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Pak Suzuki Motors Co Ltd.", "ldcp": 148.22, "open": 148.9, "high": 149.0, "low": 146.51, "current": 147.0, "change": -1.22, "volume": 42769.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Al-Ghazi Tractors Limited.", "ldcp": 342.0, "open": 347.9, "high": 349.99, "low": 347.9, "current": 349.99, "change": 7.99, "volume": 500.0, "date_time": "2022-12-08 11:59:05"}
        ]
        self.trader = TraderFactory.create()
        self.user_login(email=self.trader.user.email, password='trader')

        client = RequestsClient()
        client.headers.update({"Secret-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYXJrZXQiOiJzdG9jayIsIm5hbWUiOiJqYW5nb19yYW5nbyIsImNpdHkiOiJrYXJhY2hpIiwiaWF0IjoxNTE2MjM5MDIyfQ.-9ijMMtccWA_0NhGfDIPsJWYUYOJuKtE9P7U6-iovDI"})
        response = client.post(path, json=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_company_list(self):

        self.test_post_dataupater()

        path = reverse('company_list')
        data = [
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Hino Pak Motor Limited.", "ldcp": 245.5, "open": 228.02, "high": 228.02, "low": 227.1, "current": 227.1, "change": -18.4, "volume": 400.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Honda Atlas Cars (Pak) Ltd.", "ldcp": 150.08, "open": 146.5, "high": 150.15, "low": 146.5, "current": 148.0, "change": -2.08, "volume": 28449.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Pak Suzuki Motors Co Ltd.", "ldcp": 148.22, "open": 148.9, "high": 149.0, "low": 146.51, "current": 147.0, "change": -1.22, "volume": 42769.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Al-Ghazi Tractors Limited.", "ldcp": 342.0, "open": 347.9, "high": 349.99, "low": 347.9, "current": 349.99, "change": 7.99, "volume": 500.0, "date_time": "2022-12-08 11:59:05"}
        ]
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('name'), data[0]["company"])
        self.assertEqual(response.data[1].get('name'), data[1]["company"])
        self.assertEqual(response.data[2].get('name'), data[2]["company"])
        self.assertEqual(response.data[3].get('name'), data[3]["company"])

    def test_graph(self):

        self.test_post_dataupater()

        data = {
            "company_id": 1,
            "from_datetime": "2022-12-06 13:05:25",
            "to_datetime": "2022-12-08 12:00:05"
        }
        market_data = [
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Hino Pak Motor Limited.", "ldcp": 245.5, "open": 228.02, "high": 228.02, "low": 227.1, "current": 227.1, "change": -18.4, "volume": 400.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Honda Atlas Cars (Pak) Ltd.", "ldcp": 150.08, "open": 146.5, "high": 150.15, "low": 146.5, "current": 148.0, "change": -2.08, "volume": 28449.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Pak Suzuki Motors Co Ltd.", "ldcp": 148.22, "open": 148.9, "high": 149.0, "low": 146.51, "current": 147.0, "change": -1.22, "volume": 42769.0, "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Al-Ghazi Tractors Limited.", "ldcp": 342.0, "open": 347.9, "high": 349.99, "low": 347.9, "current": 349.99, "change": 7.99, "volume": 500.0, "date_time": "2022-12-08 11:59:05"}
        ]
        path = reverse("company_graph")
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        graph_data = json.loads(response.content)

        path = reverse('company_list')
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.get(path)

        self.assertEqual(graph_data[0].get('category_id'), response.data[0]["category"]["id"])
        self.assertEqual(graph_data[0].get('category_name'), response.data[0]["category"]["name"])

        self.assertEqual(graph_data[0].get('company_id'), response.data[0]["id"])
        self.assertEqual(graph_data[0].get('company_name'), market_data[0]["company"])
        self.assertEqual(graph_data[1][0].get('ldcp'), market_data[0]["ldcp"])
        self.assertEqual(graph_data[1][0].get('open'), market_data[0]["open"])
        self.assertEqual(graph_data[1][0].get('high'), market_data[0]["high"])
        self.assertEqual(graph_data[1][0].get('low'), market_data[0]["low"])
        self.assertEqual(graph_data[1][0].get('current'), market_data[0]["current"])
        self.assertEqual(graph_data[1][0].get('change'), market_data[0]["change"])
        self.assertEqual(graph_data[1][0].get('volume'), market_data[0]["volume"])
        self.assertEqual(graph_data[1][0].get('date_time'), market_data[0]["date_time"].replace(' ', 'T'))



