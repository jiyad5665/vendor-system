from django.urls import path


from api.v1.purchase import views

app_name="purchase"

urlpatterns=[
    path("",views.create_new_purchase),
    path("",views.purchase_list),
    path("<int:id>/",views.details_purchas),
    path('<int:id>/',views.purchase_update),
    path('<int:id>/',views.purchase_delete),
    ]


