from django.urls import path


from api.v1.vendors import views

app_name="vendors"

urlpatterns= [
    path("",views.vendor),
    path('<int:id>/',views.vendor_update),
    path('<int:id>/perfomance/',views.perfomance),

]

