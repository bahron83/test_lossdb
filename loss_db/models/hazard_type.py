from django.db import models


class Hazard(models.Model):
    id = models.AutoField(primary_key=True)
    mnemonic = models.CharField(max_length=30, null=False, blank=False,
                                db_index=True)
    title = models.CharField(max_length=80, null=False, blank=False)
    order = models.IntegerField()
    description = models.TextField(default='')

    def __unicode__(self):
        return u"{0}".format(self.mnemonic)