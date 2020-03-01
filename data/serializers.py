from rest_framework import serializers
from data.models import Data,Customer

class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id','name','campany','rate']

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','mobile','address','debit','credit']