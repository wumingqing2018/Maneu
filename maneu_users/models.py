from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(unique=True, max_length=16)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.IntegerField()
    level = models.IntegerField()
    state = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'maneu_users'
