from django.db import models


dimensions = (('dim1', 'dim1'), ('dim2', 'dim2'), ('dim3', 'dim3'))

class DamageType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False,
                            db_index=True)
    abstract = models.TextField()
    unit = models.CharField(max_length=30)    

    def __unicode__(self):
        return u"{0}".format(self.name)

class DamageTypeValue(models.Model):
    id = models.AutoField(primary_key=True)
    damage_assessment = models.ForeignKey('DamageAssessment')
    damage_type = models.ForeignKey(DamageType)
    sendai_indicator = models.ForeignKey('SendaiIndicator', blank=True, null=True)
    dimension = models.CharField(max_length=50, choices=dimensions)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0}".format(self.value)
