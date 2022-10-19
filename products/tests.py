import json
from django.test import TestCase
from .models import Product
from .serializers import ProductSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

client = APIClient()

class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Product.objects.create(
            title='test title', description='test description', details='test details', specs='test specs', price=123.45, images='test images')
        Product.objects.create(
            title='test title', description='test description', details='test details', specs='test specs', price=123.45, images='test images')
        Product.objects.create(
            title='test title', description='test description', details='test details', specs='test specs', price=123.45, images='test images')

    def test_get_all_products(self):
        response = client.get(reverse('get_post_products'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleProductTest(TestCase):
    """ Test module for GET single product API """

    def setUp(self):
        self.product = Product.objects.create(
            title='test title', description='test description', details='test details', specs='test specs', price=123.45, images='test images')
        self.product.save()

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': self.product.pk}))
        product = Product.objects.get(pk=self.product.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            'title': 'test title',
            'description': 'test description',
            'details': 'test details',
            'specs': 'test specs',
            'price': 123.45,
            'images': 'test images'
        }
        self.invalid_payload = {
            'title': '',
            'description': '',
            'details': '',
            'specs': '',
            'price': '',
            'images': ''
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)