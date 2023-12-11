from django.db import models
# from vendors.models import vendors



class Vendor(models.Model):
    name=models.CharField(max_length=150,unique=True)
    contact_details=models.TextField()
    address=models.TextField()
    vender_code=models.CharField(max_length=150,unique=True)
    on_time_delivery_rate=models.FloatField(default=0)
    quality_rating_avg=models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfilment_rate=models.FloatField(default=0)

   
    
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
    on_time_delivery_rate=models.FloatField(default=0)
    quality_rating_avg=models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfilment_rate=models.FloatField(default=0)


    class Meta:
        db_table = 'vendors_perfomance'
        verbose_name='perfomance'
        verbose_name_plural='perfomances'
        ordering= ('-id',)

    def __str__(self):
        return self.vendor.name

