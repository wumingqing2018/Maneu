# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid

from django.db import models


class ManeuAdmin(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=36)
    nickname = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    level = models.CharField(max_length=36)
    state = models.CharField(max_length=36)
    time = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=512, blank=True, null=True)
    location = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maneu_admin'
        unique_together = (('id', 'username'),)


class ManeuGuest(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    admin_id = models.CharField(max_length=36, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=36, blank=True, null=True)
    age = models.CharField(max_length=36, blank=True, null=True)
    dfh = models.CharField(max_length=36, blank=True, null=True)
    ot = models.CharField(max_length=36, blank=True, null=True)
    em = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maneu_guest'


class ManeuOrder(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    admin_id = models.CharField(max_length=36)
    guest_id = models.CharField(max_length=36)
    store_id = models.CharField(max_length=36)
    report_id = models.CharField(max_length=36)
    time = models.DateTimeField()
    name = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    remark = models.CharField(max_length=512)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maneu_order'


class ManeuReport(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    admin_id = models.CharField(max_length=36, blank=True, null=True)
    guest_id = models.CharField(max_length=36, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maneu_report'


class ManeuService(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    order_id = models.CharField(max_length=36, blank=True, null=True)
    admin_id = models.CharField(max_length=36)
    guess_id = models.CharField(max_length=36)
    content = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maneu_service'


class ManeuStore(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    order_id = models.CharField(max_length=36)
    admin_id = models.CharField(max_length=36)
    guess_id = models.CharField(max_length=36)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_store'


class ManeuUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    nickname = models.CharField(max_length=36)
    username = models.CharField(unique=True, max_length=36)
    password = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    level = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    localtion = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maneu_users'