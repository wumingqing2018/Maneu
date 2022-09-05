from django.db import models


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'meneu_store'
