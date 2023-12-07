from rest_framework.serializers import ModelSerializer
from vendors.models import Vendor
from vendors.models import Perfomance

class perfomancesSerializer(ModelSerializer):
    
    class Meta:
        fields=("vendor","date","on_time_delivery_date","quality_rating_avg","average_respose_time","fulfilment_rate")
        model=Perfomance

class VendorsSerializer(ModelSerializer):
    
    class Meta:
        fields=("name","contact_details","address","vender_code","on_time_delivery_rate","quality_rating_avg","average_response_time","fulfilment_rate")
        model=Vendor