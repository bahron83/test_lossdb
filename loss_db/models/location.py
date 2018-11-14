from django.db import models
from django.contrib.gis.db import models as gismodels
from mptt.models import MPTTModel, TreeForeignKey


location_types = (('fiexd_asset', 'fixed_asset'), ('non_fixed_asset', 'non_fixed_asset'), ('people', 'people'),)

class AdministrativeDivision(MPTTModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30, null=False, unique=True,
                            db_index=True)
    name = models.CharField(max_length=100, null=False, blank=False,
                            db_index=True)
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = gismodels.MultiPolygonField(srid=4326)
    level = models.IntegerField()
    # Relationships
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')

    def __unicode__(self):
        return u"{0}".format(self.code)

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_type = models.CharField(max_length=50, choices=location_types)
    address = models.CharField(max_length=100)    
    lat = models.CharField(max_length= 100)
    lon = models.CharField(max_length= 100)
    additional_info = models.TextField(blank=True, null=True)
    administrative_division = models.ForeignKey('AdministrativeDivision', blank=True, null=True)

    def __unicode__(self):
        return u"type: {0} - adm_unit: {1} - lat: {2} - lon: {3}".format(self.location_type, self.administrative_division, self.lat, self.lon)