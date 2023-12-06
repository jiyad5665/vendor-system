from rest_framework.serializer import ModelSerializer
from vendors.models import Vendor

class VendorsSerializer(ModelSerializer):
    
    class Meta:
        fields=("vendor","date","on_time_delivery_date","quality_rating_avg","average_respose_time","fulfilment_rate")
        Model=Vendor