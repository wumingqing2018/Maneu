import uuid

from django.db import models


# Create your models here.
class ManeuAftersales(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    order_id = models.CharField(max_length=36)
    content = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maneu_afterSales'
