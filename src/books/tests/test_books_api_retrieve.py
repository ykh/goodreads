from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models.book import Book
from books.services.books_svc import BooksService
from users.services.serializers.signup_srl import UsersSVCSignUpVLD
from users.services.users_svc import UsersService


class BooksSVCRetrieveTestCases(APITestCase):
    def setUp(self):
        self.User = get_user_model()

        self.users_svc = UsersService()
        self.books_svc = BooksService()

        self.user1 = self.users_svc.signup(
            params=UsersSVCSignUpVLD(
                data={
                    'email': 'user1@email.com',
                    'password': '123qwe!@#QWE',
                }
            )
        )

        auth_url = reverse('auth_token')

        response = self.client.post(
            path=auth_url,
            data={
                'email': 'user1@email.com',
                'password': '123qwe!@#QWE',
            },
        )

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

        self.book1 = Book.objects.create(
            title='Book 1',
            author='Author 1',
            isbn='1234567890123',
            summary='Summary 1'
        )

    def test_retrieve_books_for_guest(self):
        self.client.credentials()
        response = self.client.get(
            reverse(
                'books-detail',
                kwargs={'pk': self.book1.id},
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.book1.id))
        self.assertEqual(response.data['title'], self.book1.title)
        self.assertEqual(response.data['summary'], self.book1.summary)

    def test_retrieve_books_for_user(self):
        response = self.client.get(
            reverse(
                'books-detail',
                kwargs={'pk': self.book1.id},
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.book1.id))
        self.assertEqual(response.data['title'], self.book1.title)
        self.assertEqual(response.data['summary'], self.book1.summary)
