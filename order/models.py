# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=16)
    token = models.CharField(max_length=32, blank=True, null=True)
    c_time = models.DateTimeField()
    c_name = models.CharField(max_length=11)
    c_phone = models.CharField(max_length=11)
    frame = models.CharField(max_length=64)
    l_glasses = models.CharField(db_column='L_glasses', max_length=64)  # Field name made lowercase.
    l_pd = models.CharField(db_column='L_pd', max_length=6)  # Field name made lowercase.
    l_add = models.CharField(db_column='L_add', max_length=6)  # Field name made lowercase.
    l_sphere = models.CharField(db_column='L_sphere', max_length=6)  # Field name made lowercase.
    l_deviation = models.CharField(db_column='L_deviation', max_length=6)  # Field name made lowercase.
    l_astigmatic = models.CharField(db_column='L_astigmatic', max_length=6)  # Field name made lowercase.
    r_glasses = models.CharField(max_length=64)
    r_pd = models.CharField(db_column='R_pd', max_length=6)  # Field name made lowercase.
    r_add = models.CharField(db_column='R_add', max_length=6)  # Field name made lowercase.
    r_sphere = models.CharField(db_column='R_sphere', max_length=6)  # Field name made lowercase.
    r_astigmatic = models.CharField(db_column='R_astigmatic', max_length=6)  # Field name made lowercase.
    r_deviation = models.CharField(db_column='R_deviation', max_length=6)  # Field name made lowercase.
    besiness = models.CharField(max_length=16)
    todo = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'order'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=16)
    username = models.CharField(unique=True, max_length=16)
    nickname = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.IntegerField()
    join_time = models.DateField()
    last_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'user'
