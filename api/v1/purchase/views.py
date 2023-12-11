

import requests

import datetime
from django.shortcuts import get_object_or_404
from purchase.models import Purchase
from .serializers import PurchaseSerializer
from vendors.models import Vendor, Perfomance

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def create_new_purchase(request):
    if request.method =="POST":
        vendor=request.data.get('vendor')
        quantity=request.data.get('quantity')
        items = request.data.get('items')
        vendor = Vendor.objects.get(id=vendor)
        last_purchase=Purchase.objects.all().first()

        if last_purchase is not None:
            id=last_purchase.id
            po_number=f"PUR00{id+1}"
        else:
            po_number="PUR001"

        purchase=Purchase.objects.create(
            po_number=po_number,
            vendor=vendor,
            quantity=quantity,
            items=items,
            status= 1,
        )
        purchase.save()
        
        response_data={
            "success_code":6000,
            "message":"purchased successfully"
        }
        return Response(response_data)
    
    elif request.method == "GET":
        instances = Purchase.objects.all()
        context={
            "request":request
            }
        serializer=PurchaseSerializer(instances,many=True,context=context)

        response_data={
            "status_code":6000,
            "data":serializer.data,
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
    
