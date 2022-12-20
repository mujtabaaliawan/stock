from rest_framework.test import APITransactionTestCase, APITestCase
from rest_framework import status
from django.urls import reverse
from favourite.test.factories import TraderFactory
import json
from rest_framework.test import RequestsClient
from rest_framework.response import Response
from unittest import mock
from core.tasks import dataupdate


def mail_mock():
    print("Mock mails sent")
    return Response(status.HTTP_200_OK)


class TestFavourite(APITransactionTestCase):

    @mock.patch('core.tasks.mail_favourite', mail_mock)
    def test_mail_send(self):
        market_data = [
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Hino Pak Motor Limited.", "ldcp": 245.5, "open": 228.02,
             "high": 228.02, "low": 227.1, "current": 227.1, "change": -18.4, "volume": 400.0,
             "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Honda Atlas Cars (Pak) Ltd.", "ldcp": 150.08,
             "open": 146.5, "high": 150.15, "low": 146.5, "current": 148.0, "change": -2.08, "volume": 28449.0,
             "date_time": "2022-12-08 11:59:05"}]
        dataupdate(market_data)


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
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Hino Pak Motor Limited.", "ldcp": 245.5, "open": 228.02,
             "high": 228.02, "low": 227.1, "current": 227.1, "change": -18.4, "volume": 400.0,
             "date_time": "2022-12-08 11:59:05"},
            {"category": "AUTOMOBILE ASSEMBLER", "company": "Honda Atlas Cars (Pak) Ltd.", "ldcp": 150.08,
             "open": 146.5, "high": 150.15, "low": 146.5, "current": 148.0, "change": -2.08, "volume": 28449.0,
             "date_time": "2022-12-08 11:59:05"}
        ]
        self.trader = TraderFactory.create()
        self.user_login(email=self.trader.user.email, password='trader')
        client = RequestsClient()
        client.headers.update({"Secret-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYXJrZXQiOiJzdG9jayIsIm5hbWUiOiJqYW5nb19yYW5nbyIsImNpdHkiOiJrYXJhY2hpIiwiaWF0IjoxNTE2MjM5MDIyfQ.-9ijMMtccWA_0NhGfDIPsJWYUYOJuKtE9P7U6-iovDI"})
        response = client.post(path, json=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_favourite(self):
        self.test_post_dataupdater()

        self.user_login(email=self.trader.user.email, password='trader')
        path = reverse('market_price')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        market_data = json.loads(response.content)
        company_id = market_data[0]["company"]["id"]

        test_data = {
            "company_id": company_id,
            "monitor_field": "current",
            "minimum_limit": 220.0,
            "maximum_limit": 230.3,
            "is_active": True
        }

        path = reverse("favourite_list_new")
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_favourite_list(self):

        self.test_post_dataupdater()

        self.user_login(email=self.trader.user.email, password='trader')
        path = reverse('market_price')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        market_data = json.loads(response.content)
        company_id = market_data[0]["company"]["id"]

        test_data = {
            "company_id": company_id,
            "monitor_field": "current",
            "minimum_limit": 220.0,
            "maximum_limit": 225.3,
            "is_active": True
        }

        path = reverse("favourite_list_new")
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        fav_data = json.loads(response.content)

        self.assertEqual(fav_data[0]["company"]["id"], test_data["company_id"])
        self.assertEqual(fav_data[0]["monitor_field"], test_data["monitor_field"])
        self.assertEqual(fav_data[0]["minimum_limit"], test_data["minimum_limit"])
        self.assertEqual(fav_data[0]["maximum_limit"], test_data["maximum_limit"])
        self.assertEqual(fav_data[0]["is_active"], test_data["is_active"])

    def test_update_favourite(self):

        self.test_post_dataupdater()

        self.user_login(email=self.trader.user.email, password='trader')
        path = reverse('market_price')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        market_data = json.loads(response.content)
        company_id = market_data[0]["company"]["id"]

        test_data = {
            "company_id": company_id,
            "monitor_field": "current",
            "minimum_limit": 220.0,
            "maximum_limit": 225.3,
            "is_active": True
        }

        path = reverse("favourite_list_new")
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        fav_data = json.loads(response.content)

        self.assertEqual(fav_data[0]["is_active"], test_data["is_active"])

        update_data = {
            "is_active": False
        }

        path = reverse('favourite_update', kwargs={'pk': fav_data[0]["id"]})
        self.user_login(email=self.trader.user.email, password='trader')
        response = self.client.patch(path, json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["is_active"], update_data["is_active"])

