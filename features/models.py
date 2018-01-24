from django.db import models
from datetime import datetime


class Client(models.Model):
	"""
	class which represents class table of DB containing all the clients info
	"""
	client_name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.client_name
	
class Product(models.Model):
	"""
	class which represents product table of Db containing all the product info
	"""
	product_area = models.CharField(max_length=200)
	
	def __str__(self):
		return self.product_area
		
class Feature(models.Model):
	"""
	class representing feature table containing all the feature details
	product and client are referenced as foreign key
	"""
	feature_title = models.CharField(max_length=200)
	feature_desc = models.TextField()
	target_date = models.DateField('date targetted')
	create_date = models.DateTimeField(default=datetime.now())
	product_area = models.ForeignKey(Product, on_delete=models.CASCADE)
	client_name = models.ForeignKey(Client,  on_delete=models.CASCADE)
	client_priority = models.IntegerField(default=0)
	
	def __str__(self):
		return self.feature_title
	