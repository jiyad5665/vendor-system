from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/',include(("api.v1.vendors.urls"))),
    path('api/purchase_orders/',include(("api.v1.purchase.urls")))
]
