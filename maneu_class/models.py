# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid


class ManeuClass(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    user_id = models.CharField(max_length=36)
    name = models.CharField(max_length=36)
    time = models.DateField()
    series = models.CharField(max_length=36)
    color = models.CharField(max_length=36)
    class_field = models.CharField(db_column='class', max_length=36)  # Field renamed because it was a Python reserved word.
    count = models.CharField(max_length=36)
    price = models.CharField(max_length=36)
    remark = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maneu_class'
