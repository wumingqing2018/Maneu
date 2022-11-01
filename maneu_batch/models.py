# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ManeuAftersales(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    order_id = models.CharField(max_length=36)
    content = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maneu_aftersales'


class ManeuBatch(models.Model):
    order_id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    c_time = models.DateTimeField()
    c_name = models.CharField(max_length=255)
    c_phone = models.CharField(max_length=255)
    order = models.TextField()
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_batch'


class ManeuClass(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
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


class ManeuDatalogs(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    user_id = models.CharField(max_length=36)
    time = models.DateField()
    order_log = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'maneu_datalogs'


class ManeuGuess(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.CharField(max_length=36)
    name = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    sex = models.CharField(max_length=36)
    age = models.CharField(max_length=36)
    ot = models.CharField(db_column='OT', max_length=36)  # Field name made lowercase.
    em = models.CharField(db_column='EM', max_length=36)  # Field name made lowercase.
    dfh = models.CharField(db_column='DFH', max_length=36)  # Field name made lowercase.
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_client'


class ManeuOrder(models.Model):
    order_id = models.CharField(primary_key=True, max_length=32)
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
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    name = models.CharField(max_length=36)
    phone = models.CharField(max_length=36)
    guess_id = models.CharField(max_length=36)
    users_id = models.CharField(max_length=36)
    store_id = models.CharField(max_length=36)
    visionsolutions_id = models.CharField(db_column='visionSolutions_id', max_length=36)  # Field name made lowercase.
    subjectiverefraction_id = models.CharField(db_column='subjectiveRefraction_id', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maneu_order_v2'


class ManeuStore(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_store'


class ManeuSubjectiveRefraction(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_subjective_refraction'


class ManeuUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    nickname = models.CharField(max_length=36)
    username = models.CharField(unique=True, max_length=36)
    password = models.CharField(max_length=36)
    localtion = models.CharField(max_length=128)
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
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_vision_solutions'
