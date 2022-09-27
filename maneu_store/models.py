from django.db import models


class ManeuStore(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    time = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'maneu_store'
