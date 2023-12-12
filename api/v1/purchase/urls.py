from django.urls import path


from api.v1.purchase import views

app_name="purchase"

urlpatterns=[
    path("",views.create_new_purchase),
    path("<int:id>/",views.details_purchas),
    path("<int:id>/issue_date/",views.update_issue_date),
    path("<int:id>/aknowlwdgment_date/",views.update_aknowledgment_date),
    path("<int:id>/delivery_date/",views.update_delivery_date),
    path("<int:id>/quality_rating/",views.update_quality_rating),
     
    ]


