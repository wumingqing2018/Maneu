# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ManeuClass(models.Model):
    # Field name made lowercase.
    classid = models.IntegerField(db_column='classID', primary_key=True)
    class_batch = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    class_brand = models.CharField(max_length=255)
    class_model = models.CharField(max_length=255)
    class_param = models.CharField(max_length=255)
    class_status = models.IntegerField()
    class_remark = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maneu_class'
