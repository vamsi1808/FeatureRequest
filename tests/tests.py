import unittest
from django.urls import reverse
from unittest.mock import patch
from features.views import FeatureList, FeatureDetail
from features.models import Feature, Client, Product

class TestDatabaseManipulations(unittest.TestCase):
	"""
	Unit test class to test database manipulations like select all, select one and insert
	
	* A small dummy database will be created in a memory which will insert data given in setUp() method
	* Database will be deleted immediately after the tests are run.
	"""
	mock_data_good = [{
				"client_name": "ClientA",
				"client_priority": 1,
				"create_date": "2018-01-16T22:16:36.105460Z",
				"feature_desc": "descA",
				"feature_title": "titleA",
				"id": 1,
				"product_area": "Product A",
				"target_date": "2018-10-10"
    }]
	mock_data_bad = []
	
	def setUp(self):
		client_data = Client.objects.create(client_name='clientA')
		product_data = Product.objects.create(product_area='product A')
		Feature.objects.create(feature_title='titleA', 
								feature_desc='descA',
								target_date='2018-10-10',
								create_date='2018-01-16T22:16:36.105460Z',
								product_area=product_data,
								client_name=client_data, 
								client_priority=1)
								
	def test_get_feature_list(self):
		with patch.object(FeatureList, "get_data", return_value=TestDatabaseManipulations.mock_data_good) as mocked_get:
			result = FeatureList.get_serialized_data(self, Feature.objects.all())
			self.assertTrue(result)
	
	def test_get_feature_detail(self):
		with patch.object(FeatureDetail, "get_object", return_value=TestDatabaseManipulations.mock_data_good[0]) as mocked_get:
			result = FeatureDetail.get_serialized_data(self, Feature.objects.get(pk=1))
			self.assertTrue(result)
	"""
	def test_feature_save(self):
		with patch.object(FeatureDetail, "get_object", return_value=TestDatabaseManipulations.mock_data_good[0]) as mocked_get:
			result = FeatureDetail.get_serialized_data(self, Feature.objects.get(pk=1))
			self.assertTrue(result)
	"""	

class TestJWTAuthentication(unittest.TestCase):
	"""
	Unit test class to test the authentication which we have implemented through JSONWebTokenAuthentication
	
	*Here, it will make a call with dummy user and get the token
	*then token will send in the header to check the status code
	"""
	def test_api_jwt(self):
		username = 'user'
		password = 'passwd'
		token = 0
		user_id = 0

		def setUp(self):
			data = {'username': self.username,
					'password': self.password,
					'email': 'email@gmail.com'}
			url = reverse('api-token-auth')
			response = self.client.post(url, data, format='json')
			self.user_id = response.data['id']

			data = {'username': self.username,
					'password': self.password}
			url = reverse('token_auth')
			response = self.client.post(url, data, format='json')
			self.token = response.data['token']

		def test_auth_user_info(self):
			data = {'id': str(self.user_id),
					'password': self.password,
					'email': 'email@gmail.com',
					'username': self.username,
					}
			url = reverse('api-token-auth', kwargs={'pk': self.user_id})
			response = self.client.patch(url, data, Authorization='JWT ' + self.token, format='son')
			self.assertEqual(response.status_code, 200)
			
	
if __name__ == '__main__':
    unittest.main()

	