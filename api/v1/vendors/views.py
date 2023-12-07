
import requests

import datetime
from purchase.models import Purchase
from .serializers import VendorsSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny



from vendors.models import Vendor,Perfomance


@api_view(["POST"])
@permission_classes([AllowAny])
def create_new_vendor(request):
    name=request.data.get('name')
    contact_details=request.data.get('contact_details')
    address=request.data.get('address')

    previous_vendor=Vendor.objects.all().first()

    if previous_vendor is not None:
        id=previous_vendor.id
        vendor_code=f"VD00{id+1}"
    else:
        vendor_code="VD001"


    vendor=Vendor.objects.create(
        name=name,
        contact_details=contact_details,
        address=address,
        vender_code=vendor_code
    )
    vendor.save()
    
    response_data={
        "success_code":6000,
        "message":"vendor created successfully"
    }

    return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def vendor_list(request):
    instances=Vendor.objects.all()
    context={
        "request":request
    }
    serializer=VendorsSerializer(instances,many=True,context=context)


    response_data={
        "status_code":6000,
        "data":serializer.data,
    }
    return Response(response_data)
    


@api_view(["GET"])
@permission_classes([AllowAny])
def details_vendor(request):
    pass


@api_view(["PUT"])
@permission_classes([AllowAny])
def vendor_update(request):
    pass

@api_view(["DELETE"])
@permission_classes([AllowAny])
def vendor_delete(request):
    pass



@api_view(["GET"])
@permission_classes([AllowAny])
def perfomance(request):
    pass