
import requests

import datetime
from purchase.models import Purchase
from .serializers import VendorsSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny



from django.shortcuts import get_object_or_404
from vendors.models import Vendor,Perfomance
from.serializers import VendorsSerializer


@api_view(["POST","GET"])
@permission_classes([AllowAny])
def vendor(request):
    if request.method =="POST":
        name=request.data.get('name')
        contact_details=request.data.get('contact_details')
        address=request.data.get('address')

        last_vendor=Vendor.objects.all().first()

        if last_vendor is not None:
           id=last_vendor.id
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
    
    elif request.method =="GET":
        instances =Vendor.objects.all()
        context={
            "request":request
            }
        serializer=VendorsSerializer(instances,many=True,context=context)

        request_data={
            "status_code":6000,
            "data":serializer.data,
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
    





@api_view(["PUT","GET","DELETE"])
@permission_classes([AllowAny])
def vendor_update(request):
    instance=get_object_or_404(Vendor, id=id)
    
    if request.method =="GET":
        context={
                "request":request
            }
        serializer=VendorsSerializer(instance,context=context)

        response_data={
            "status_code":6000,
            "data":serializer.data,
        }
        return Response(response_data)

    elif  request.method =="PUT":
        
        name =request.data.get("name")
        contact_details=request.data.get("contact_details")
        address=request.data.get("address")

        if name is not None:
            instance.name=name
            instance.save()

        if contact_details is not None:
            instance.contact_details=name
            instance.save()

        if address is not None:
            instance.address=name
            instance.save()
        
        response_data={
            "success_code":6000,
            "message":"vender updated succesfully"
        }

        return Response(response_data)
    elif request.method =="DELETE":
        instance.delete()

        response_data={
            "success_code":6000,
            "message":"vender deleted succesfully"
        }
        return Response(response_data)




 



@api_view(["GET"])
@permission_classes([AllowAny])
def perfomance(request):
    pass