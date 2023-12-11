

import requests

import datetime
from django.shortcuts import get_object_or_404
from purchase.models import Purchase
from .serializers import PurchaseSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def create_new_purchase(request):
     if request.method =="POST":
        name=request.data.get('name')
        contact_details=request.data.get('contact_details')
        address=request.data.get('address')

        last_Purchase=Purchase.objects.all().first()

        if last_Purchase is not None:
           id=last_Purchase.id
           Purchase_code=f"VD00{id+1}"
        else:
          Purchase_code="VD001"
        Purchase=Purchase.objects.create(
            name=name,
            contact_details=contact_details,
            address=address,
            Purchase_code=Purchase_code
        )
        Purchase.save()
        
        response_data={
            "success_code":6000,
            "message":"purchase created successfully"
        }
        return Response(response_data)



@api_view(["GET","PUT","DELETE"])
@permission_classes([AllowAny])
def details_purchas(request, id):
    instance=get_object_or_404(Purchase, id=id)
    if request.method =="GET":
        context={
                "request":request
            }
        serializer=PurchaseSerializer(instance,context=context)

        response_data={
            "status_code":6000,
            "data":serializer.data,
        }
        return Response(response_data)
    elif  request.method =="PUT":
        pass

    elif request.method =="DELETE":
        instance.delete()

        response_data={
            "success_code":6000,
            "message":"purchase deleted succesfully"
        }
        return Response(response_data)
    
