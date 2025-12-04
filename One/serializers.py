from rest_framework.serializers import ModelSerializer
from . models import Users, Orders, Products



class Users_serializer(ModelSerializer):
    class Meta:
        model= Users
        fields= '__all__'

        

class Orders_serializer(ModelSerializer):

    class Meta:
        model = Orders
        fields= '__all__'



class Product_serializer(ModelSerializer):

    class Meta:
        model = Products
        fields= '__all__'
