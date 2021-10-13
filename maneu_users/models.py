# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' maneu_order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    level = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maneu_users'
