from django.db import models


scopes = (('risk', 'risk'), ('event', 'event'),)

class AnalysisType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False,
                            db_index=True)
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(default='', null=True, blank=False)    
    scope = models.CharField(max_length=25, choices=scopes, default=scopes[0])

    def __unicode__(self):
        return u"{0}".format(self.name)