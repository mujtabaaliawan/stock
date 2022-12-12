from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from user.test.factories import UserFactory
import json


class TestUser(APITestCase):

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

    def test_create_user(self):
        test_data = {
            "email": "john@gmail.com",
            "first_name": "John",
            "last_name": "Smith",
            "password": "john",
            "role": "client",
        }

        path = reverse('user_new')

        self.user = UserFactory.create()
        self.user_login(email=self.user.email, password='user')
        response = self.client.post(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list(self):
        path = reverse('user_list')

        self.user = UserFactory.create()
        self.user_login(email=self.user.email, password='user')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0].get('first_name'), self.user.first_name)
        self.assertEqual(response.data[0].get('last_name'), self.user.last_name)
        self.assertEqual(response.data[0].get('email'), self.user.email)
        self.assertEqual(response.data[0].get('role'), self.user.role)


    def test_update_user(self):

        test_data = {
            "first_name": "mujtaba"
        }
        self.user = UserFactory.create()

        path = reverse('user_list')
        self.user_login(email=self.user.email, password='user')
        response = self.client.get(path)
        self.assertEqual(response.data[0].get('first_name'), self.user.first_name)

        path = reverse('user_update', kwargs={'pk': self.user.id})
        self.user_login(email=self.user.email, password='user')
        response = self.client.patch(path, json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), test_data['first_name'])
