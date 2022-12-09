import uuid

from django.db import models


class ManeuGuess(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    user_id = models.CharField(max_length=36)
    subjective_id = models.CharField(max_length=36)
    time = models.DateTimeField()
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
        db_table = 'maneu_guess'


class ManeuSubjectiveRefraction(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_subjective_refraction'


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
