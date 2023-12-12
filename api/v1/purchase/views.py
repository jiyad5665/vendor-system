

import requests

import datetime
from django.shortcuts import get_object_or_404
from purchase.models import Purchase
from .serializers import PurchaseSerializer
from vendors.models import Vendor, Perfomance
from django.db.models import Sum

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(["POST","GET"])
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
    
@api_view(["PUT"])
@permission_classes([AllowAny])
def update_issue_date(request,id):
    instance=get_object_or_404(Purchase,id=id)
    date=datetime.datetime.today()

    instance.issue_date=date
    instance.save()

    response_data={
            "success_code":6000,
            "message":"issue date completed"
        }
    return Response(response_data)
    

    

    
@api_view(["PUT"])
@permission_classes([AllowAny])
def update_aknowledgment_date(request,id):
    instance=get_object_or_404(Purchase,id=id)

    date=request.data.get('date')

    aknowledgment_date=datetime.datetime.today()

    instance.expected_deliverydate=date
    instance.aknowledjment_date=aknowledgment_date
    instance.save()

    vendor=instance.vendor

    total_purchases=Purchase.objects.filter(vendor=vendor)
    total_purchases_count=total_purchases.count()

    total_response_time = 0

    if total_purchases_count > 0:
        total_response_time = 0

        for purchase in total_purchases:
            issue_date = purchase.issue_date
            acknowledgment_date = purchase.aknowledjment_date

            if issue_date is not None and acknowledgment_date is not None:
                response_time = (acknowledgment_date - issue_date).total_seconds()
                total_response_time += response_time

        average_response_time = total_response_time / total_purchases_count
    else:
        average_response_time = 0 

    vendor.average_response_time = average_response_time / 60

    vendor.save()

    average_response_time = total_response_time / total_purchases_count
    vendor.average_response_time=average_response_time
    vendor.save()

    perfomnace=get_object_or_404(Perfomance,vendor=vendor)
    perfomnace.average_response_time =average_response_time
    perfomnace.save()

    
    

    response_data={
        "success_code":6000,
        "message":"Delivery date updated"

    }

    return Response(response_data)
    

    
@api_view(["PUT"])
@permission_classes([AllowAny])
def update_delivery_date(request,id):
    instance=get_object_or_404(Purchase,id=id)

    date=datetime.datetime.today()
    instance.deliverydate=date
    instance.status=2
    instance.save()

    vendor=instance.vendor

    total_purchase=Purchase.objects.filter(vendor=vendor)
    purchase_count=total_purchase.count()
    complete_purchase=total_purchase.filter(status=2)
    complete_purchase_count = complete_purchase.count()

    fulfilment=complete_purchase_count/purchase_count
    on_time_deliveries = 0

    for purchase in complete_purchase:
        expeted_delivery_date = purchase.expected_deliverydate
        delivery_date = purchase.deliverydate

        if delivery_date <= expeted_delivery_date:
            on_time_deliveries += 1

    on_time_delivery_rate = (on_time_deliveries / complete_purchase_count) * 100

    vendor.fulfilment_rate = fulfilment
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.save()

    perfomance=get_object_or_404(Perfomance,vendor=vendor)
    perfomance.fulfilment_rate =fulfilment
    perfomance.on_time_delivery_rate = on_time_delivery_rate
    perfomance.save()


    response_data={
         "success_code":6000,
            "message":"Delivery date updated"

    }

    return Response(response_data)
    

    
@api_view(["PUT"])
@permission_classes([AllowAny])
def update_quality_rating(request,id):
    instance=get_object_or_404(Purchase,id=id)

    rate=request.data.get('rate')

    if int(rate) > 5:
        rate=5

    instance.quality_rating=rate
    instance.save()

    vendor =instance.vendor

    total_purchases=Purchase.objects.filter(vendor=vendor)
    purchase_count=total_purchases.count()
    total_quality_rating=total_purchases.aggregate(Sum("quality_rating"))["quality_rating__sum"]
    vendor_rating=total_quality_rating/purchase_count

    vendor.quality_rating_avg=vendor_rating

    perfomance=get_object_or_404(Perfomance,vendor=vendor)
    perfomance.quality_rating_avg=vendor_rating
    perfomance.save()


    response_data={
         "success_code":6000,
            "message":"quality rate updated"

    }

    return Response(response_data)
    
