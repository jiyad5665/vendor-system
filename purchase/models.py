from django.db import models
from vendors.models import Vendor 
 
class Purchase(models.Model):
    po_number=models.CharField(max_length=150)
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    deliverydate=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField()
    quality_rating=models.FloatField()
    issue_date=models.DateTimeField()
    aknowledjment_date=models.DateTimeField()


    class Meta:
        db_table = 'purchase_purchase'
        verbose_name='purchase'
        verbose_name_plural='purchases'
        ordering= ('-id',)

    def __str__(self):
        return self.po_number    

    