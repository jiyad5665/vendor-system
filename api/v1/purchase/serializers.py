from purchase.models import Purchase
from rest_framework.serializers import ModelSerializer

class PurchaseSerializer(ModelSerializer):
    class Meta:
        fields= ("id","po_number","vendor","order_date","deliverydate","items","quantity","status","quality_rating","issue_date","aknowledjment_date")
        model=Purchase