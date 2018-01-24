from rest_framework import serializers
from features.models import Feature, Client, Product

class ProductSerializer(serializers.ModelSerializer):
	"""
	Serialization class for Product model
	
	*While fetching feature detail, we just need product area name
	*whereas which fetching product detail to show in dropdown in UI, we need full detail
	*therefore based on the value of "list" received, 
	*it decides whether to send full detail or just product area name
	"""
	def to_representation(self, value):
		list = self.context.get("list")
		if list:
			return {'id':value.id,'product_area':value.product_area}
		else:
			return value.product_area
			
	class Meta:
		model = Product
		fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
	"""
	Serialization class for Client model
	
	*Based on the value of "list" received, 
	*it decides whether to send full detail or just client name
	"""
	def to_representation(self, value):
		list = self.context.get("list")
		if list:
			return {'id':value.id,'client_name':value.client_name}
		else:
			return value.client_name
			
	class Meta:
		model = Client
		fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
	"""
	Serialization class for Feature Model
	"""
	product_area = ProductSerializer()
	client_name = ClientSerializer()

	class Meta:
		model = Feature
		fields = ('id','feature_title','feature_desc','target_date','create_date','product_area','client_name','client_priority')

			