from django.urls import path


from api.v1.purchase import views

app_name="purchase"

urlpatterns=[
    path("",views.create_new_purchase),
    path("<int:id>/",views.details_purchas),
    ]


