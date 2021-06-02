from django.db import models


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=64)
    token = models.CharField(max_length=64, blank=True, null=True)
    c_time = models.DateTimeField()
    c_name = models.CharField(max_length=11)
    c_phone = models.CharField(max_length=11)
    order = models.TextField(blank=True, null=True)
    besiness = models.CharField(max_length=16)
    todo = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'order'
