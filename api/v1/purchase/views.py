

import requests

import datetime
from purchase.models import Purchase

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def create_new_purchase(request):
    pass


@api_view(["GET"])
@permission_classes([AllowAny])
def purchase_list(request):
    pass


@api_view(["GET"])
@permission_classes([AllowAny])
def details_purchas(request):
    pass


@api_view(["PUT"])
@permission_classes([AllowAny])
def purchase_update(request):
    pass


@api_view(["DELETE"])
@permission_classes([AllowAny])
def purchase_delete(request):
    pass