from django.db import models


class FrameworkStore(models.Model):
    store_id = models.CharField(primary_key=True, max_length=32)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    count = models.CharField(max_length=255)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'framework_store'


class GlassStore(models.Model):
    store_id = models.CharField(primary_key=True, max_length=32)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    sphere = models.CharField(max_length=255)
    astigmatic = models.CharField(max_length=255)
    refraction = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, blank=True, null=True)
    qrcode = models.CharField(unique=True, max_length=255, blank=True, null=True)
    count = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'glass_store'
