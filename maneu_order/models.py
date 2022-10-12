# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' maneu_order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid

from django.db import models


class ManeuBatch(models.Model):
    order_id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    c_time = models.DateTimeField()
    c_name = models.CharField(max_length=255)
    c_phone = models.CharField(max_length=255)
    order = models.TextField()
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_batch'


class ManeuGuess(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    sex = models.CharField(max_length=32)
    age = models.DateField()
    ot = models.CharField(db_column='OT', max_length=32)  # Field name made lowercase.
    em = models.CharField(db_column='EM', max_length=32)  # Field name made lowercase.
    dfh = models.CharField(db_column='DFH', max_length=32)  # Field name made lowercase.
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_guess'


class ManeuOrder(models.Model):
    order_id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    order_token = models.CharField(max_length=32, blank=True, null=True)
    c_time = models.DateTimeField()
    c_name = models.CharField(max_length=11)
    c_phone = models.CharField(max_length=11)
    order = models.TextField(blank=True, null=True)
    besiness = models.CharField(max_length=16)
    status = models.IntegerField()
    remark = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'maneu_order'


class ManeuOrderV2(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    name = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    guess_id = models.CharField(db_column='guess_id', max_length=36)
    users_id = models.CharField(db_column='users_id', max_length=36)
    store_id = models.CharField(db_column='store_id', max_length=36)
    visionsolutions_id = models.CharField(db_column='visionSolutions_id', max_length=36)  # Field name made lowercase.
    subjectiverefraction_id = models.TextField(db_column='subjectiveRefraction_id',
                                               max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maneu_order_v2'


class ManeuStore(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_store'


class ManeuSubjectiveRefraction(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_subjective_refraction'


class ManeuUsers(models.Model):
    user_id = models.CharField(primary_key=True, max_length=36)
    nickname = models.CharField(max_length=36)
    username = models.CharField(unique=True, max_length=36)
    password = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    level = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()
    remark = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maneu_users'


class ManeuVisionSolutions(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_vision_solutions'


class ManeuAfterSales(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    order_id = models.CharField(max_length=36)
    content = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maneu_afterSales'


class ManeuDatalogs(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid1, editable=False)
    user_id = models.CharField(max_length=36)
    time = models.DateField()
    order_log = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_datalogs'
