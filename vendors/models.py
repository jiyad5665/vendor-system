from django.db import models
# from vendors.models import vendors



class Vendor(models.Model):
    name=models.CharField(max_length=150)
    contact_details=models.TextField()
    address=models.TextField()
    vender_code=models.CharField(max_length=150)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfilment_rate=models.FloatField()

   
    
    class Meta:
        db_table = 'vendors_vendor'
        verbose_name='vendor'
        verbose_name_plural='vendors'
        ordering= ('-id',)

    def __str__(self):
        return self.name



class Perfomance(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date=models.DateTimeField()
    on_time_delivery_date=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_respose_time=models.FloatField()
    fulfilment_rate=models.FloatField()


    class Meta:
        db_table = 'vendors_perfomance'
        verbose_name='perfomance'
        verbose_name_plural='perfomances'
        ordering= ('-id',)

    def __str__(self):
        return self.vendor

