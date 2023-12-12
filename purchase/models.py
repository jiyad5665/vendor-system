from django.db import models
from vendors.models import Vendor 


STATUS_CHOICES = (
    ("1","pending"),
    ("2","completed"),
    ("3","cancelled"),

)
 
class Purchase(models.Model):
    po_number=models.CharField(max_length=150)
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now=True)
    deliverydate=models.DateTimeField(blank=True, null=True)
    expected_deliverydate=models.DateTimeField(blank=True, null=True)
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=25,choices=STATUS_CHOICES)
    quality_rating=models.FloatField(blank=True, null=True)
    issue_date=models.DateTimeField(blank=True, null=True)
    aknowledjment_date=models.DateTimeField(blank=True, null=True)


    class Meta:
        db_table = 'purchase_purchase'
        verbose_name='purchase'
        verbose_name_plural='purchases'
        ordering= ('-id',)

    def __str__(self):
        return self.po_number    

    