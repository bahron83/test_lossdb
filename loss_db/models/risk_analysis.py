from django.db import models
from loss_db.models.risk_app import RiskAppAware
from loss_db.models.entity import OwnedModel, Schedulable, LocationAware, HazardTypeAware, AnalysisTypeAware, Exportable


class DamageAssessment(OwnedModel, RiskAppAware, Schedulable, LocationAware, HazardTypeAware, AnalysisTypeAware, Exportable):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False,
                            db_index=True)
    unit_of_measure = models.CharField(max_length=255, null=True, blank=True)    
    tags = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255)
    begin_date = models.DateField()

    hazard = models.ForeignKey(
        'Hazard',
        related_name='riskanalysis_hazard',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    
    analysis_type = models.ForeignKey(
        'AnalysisType',
        related_name='riskanalysis_analysistype',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    damage_types = models.ManyToManyField('DamageType', through='DamageTypeValue')
    items = models.ManyToManyField('AssetItem', through='DamageAssessmentValue', through_fields=('damage_assessment','item'), related_name='assessment_for_item')
    phenomena = models.ManyToManyField('Phenomenon', through='DamageAssessmentValue', related_name='assessment_for_phenomenon')

    def __unicode__(self):
        return u"{0}".format(self.name)

class DamageAssessmentValue(models.Model):
    id = models.AutoField(primary_key=True)
    damage_assessment = models.ForeignKey(DamageAssessment)
    damage_type_value_1 = models.ForeignKey(
        'DamageTypeValue',
        related_name='assessment_dim1'
    )
    damage_type_value_2 = models.ForeignKey(
        'DamageTypeValue',
        related_name='assessment_dim2'
    )
    damage_type_value_3 = models.ForeignKey(
        'DamageTypeValue',
        related_name='assessment_dim3',        
        blank=True,
        null=True
    )
    phenomenon = models.ForeignKey('Phenomenon')
    item = models.ForeignKey('AssetItem', related_name='assessed_damage')
    linked_item = models.ForeignKey(
        'AssetItem',
        related_name='related_assessed_damage',
        blank=True,
        null=True
    )
    value = models.DecimalField(decimal_places=2, max_digits=10)
    #this allows to localise non static assets at the moment of the impact
    location = models.ForeignKey(
        'Location',
        related_name='damage_location',        
        blank=True,
        null=True
    )