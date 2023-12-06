
import requests

import datetime
from purchase.models import Purchase

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny



from vendors.models import Vendor,Perfomance


@api_view(["POST"])
@permission_classes([AllowAny])
def create_new_vendor(request):
    pass


@api_view(["GET"])
@permission_classes([AllowAny])
def vendor_list(request):
    pass


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