from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .forms import Contacto

# Create your tests here.

class TestCase1(TestCase):
	def test_view(self):
		response = self.client.get(reverse('user'))
		self.assertEqual(response.status_code,302)

class TestLogin(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('john', 'john@doe.com', 'johnpasswd')

	def test_login(self):
		self.client.login(username='john', password='johnpasswd')
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code,200)

class TestForm(TestCase):
	def test_valid_form (self):
		data = {'name':'Carlos','email':'carlos@aqui.com','comment':'Prueba'}
		form = Contacto(data)
		self.assertTrue(form.is_valid())

	def test_invalid_form (self):
		data = {'name':'Carlos','email':'Carlos','comment':'Prueba'}
		form = Contacto(data)
		self.assertFalse(form.is_valid())
