from django.urls import path


from api.v1.vendors import views

app_name="vendors"

urlpatterns=[
    path("",views.create_new_vendor),
    path("",views.vendor_list),
    path("<int:id>/",views.details_vendor),
    path('<int:id>/',views.vendor_update),
    path('<int:id>/',views.vendor_delete),
    path('<int:id>/',views.vendor_update),
    path('<int:id>/perfomance',views.perfomance),

]

