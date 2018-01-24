from features.models import Feature, Product, Client
from features.serializer import FeatureSerializer, ProductSerializer, ClientSerializer
from django.http import Http404
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework import permissions
from django.db.models import F
from django.db import IntegrityError, transaction
import json

import logging
errorlog = logging.getLogger("error_logger")
infolog = logging.getLogger("info_logger")

class FeatureList(APIView):
	"""
    View to list all features available.

    * Requires token authentication.
    * Only authorized users are able to access this view.
    """
	permission_classes = (permissions.IsAuthenticated,)
	
	def get_data(self):
		"""
		Separate method to fetch all the feature data from db
		"""
		try:
			return Feature.objects.all()
		except Feature.DoesNotExist as e:
			errorlog.error(repr(e))
			raise Http404
	
	def get_serialized_data(self, features):
		"""
		method to serialize feature data and return json converted data
		*features: list of Feature objects
		"""
		serializer = FeatureSerializer(features, many=True)
		serializer_data = serializer.data
		return serializer_data
		
	def get(self, request):
		"""
        Return a list of all the features.
        """
		infolog.info("GET: Feature List request received")
		try:
			features = self.get_data()
			serializer_data = self.get_serialized_data(features)
			data = json.loads(json.dumps(serializer_data))
			return Response(data)
		except Exception as e:
			content = {'Error': 'Error in returning feature list'}
			errorlog.error(repr(e))
			return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
class FeatureDetail(APIView):
	"""
    View to fetch and add feature details.

    * Requires token authentication.
    * Only authorized users are able to access this view.
    """
	permission_classes = (permissions.IsAuthenticated,)
	
	def get_object(self, pk):
		"""
		Method to fetch feature details from database
		"""
		try:
			return Feature.objects.get(pk=pk)
		except Feature.DoesNotExist as e:
			errorlog.error(repr(e))
			raise Http404
	
	def get_serialized_data(self, features):
		"""
		Method to serialize feature object
		*features: feature object
		"""
		serializer = FeatureSerializer(features)
		serializer_data = serializer.data
		return serializer_data
		
	def get(self, request, pk):
		"""
        Get method to return a feature detail.
        """
		infolog.info("GET: Feature Detail request received")
		try:
			features = self.get_object(pk)
			serializer_data = self.get_serialized_data(features)
			print(serializer_data)
			return Response(serializer_data)
		except Exception as e:
			content = {'Error': 'Error in returning feature detail'}
			errorlog.error(repr(e))
			return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
	def post(self, request):
		"""
		Post method to add new feature into database
		
		*Queries will execute in atomic transactional manner.
		*Everything will be rollbacked in case of any issue
		"""
		client_id = request.data['client_id']
		product_id = request.data['product_id']
		feature_title = request.data['feature_title'].strip()
		feature_desc = request.data['feature_desc'].strip()
		target_date = request.data['target_date']
		priority = request.data['priority']
		
		try:
			with transaction.atomic():
				""" If same priority is set, then reorder all other feature requests for this client"""
				feature_same_priority = Feature.objects.filter(client_name__id=client_id).filter(client_priority__gte=priority)
				if feature_same_priority.count() > 0:
					 feature_same_priority.update(client_priority=F('client_priority')+1)
					 
				try:
					client = Client.objects.get(pk=client_id)
				except Client.DoesNotExist as e:
					errorlog.error(repr(e))
					raise Http404
				try:
					product = Product.objects.get(pk=product_id)
				except Product.DoesNotExist as e:
					errorlog.error(repr(e))
					raise Http404
					
				""" Save feature data into database """
				feature = Feature.objects.create(feature_title=feature_title, 
										feature_desc=feature_desc, 
										target_date = target_date, 
										client_priority=priority, 
										client_name=client, 
										product_area=product)
				serializer = FeatureSerializer(feature)
				serializer_data = serializer.data
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		except IntegrityError as e:
			content = {'Error': repr(e)}
			errorlog.error(repr(e))
			return Response(content, status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):
	"""
    View to list all product area available.

    * Requires token authentication.
    * Only authorized users are able to access this view.
    """
	permission_classes = (permissions.IsAuthenticated,)
	
	def get_data(self):
		try:
			return Product.objects.all()
		except Product.DoesNotExist as e:
			errorlog.error(repr(e))
			raise Http404
	
	def get_serialized_data(self, products):
		serializer = ProductSerializer(products, many=True, context={'list': True})
		serializer_data = serializer.data
		return serializer_data
		
	def get(self, request):
		"""
        Return a list of all the Product areas.
        """
		infolog.info("GET: Product List request received")
		try:
			products = self.get_data()
			serializer_data = self.get_serialized_data(products)
			return Response(serializer_data)
		except Exception as e:
			content = {'Error': 'Error in returning products list'}
			errorlog.error(repr(e))
			return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

			
class ClientList(APIView):
	"""
    View to list all the clients available.

    * Requires token authentication.
    * Only authorized users are able to access this view.
    """
	permission_classes = (permissions.IsAuthenticated,)
	
	def get_data(self):
		try:
			return Client.objects.all()
		except Client.DoesNotExist as e:
			errorlog.error(repr(e))
			raise Http404
	
	def get_serialized_data(self, clients):
		serializer = ClientSerializer(clients, many=True, context={'list': True})
		serializer_data = serializer.data
		return serializer_data
		
	def get(self, request):
		"""
        Return a list of all the client names.
        """
		infolog.info("GET: Product List request received")
		try:
			clients = self.get_data()
			serializer_data = self.get_serialized_data(clients)
			return Response(serializer_data)
		except Exception as e:
			content = {'Error': 'Error in returning clients list'}
			errorlog.error(repr(e))
			return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
			
class ViewScreen(APIView):
	def get(self, request, pk):
		return render_to_response('EditList.html',{'feature_id':pk})