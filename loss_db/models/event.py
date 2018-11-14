from django.db import models
from loss_db.models.risk_app import RiskAppAware
from loss_db.models.entity import LocationAware, HazardTypeAware, Exportable, Schedulable
from loss_db.models import (EntityAbstract, AttributeValueVarchar, AttributeValueText,
                                AttributeValueInt, AttributeValueDecimal, AttributeValueDate)


DEFAULT_ENTITY_TYPE = 'event'

class EventAttributeValueVarchar(AttributeValueVarchar):    
    event = models.ForeignKey('Event')    

class EventAttributeValueText(AttributeValueText):    
    event = models.ForeignKey('Event')    

class EventAttributeValueInt(AttributeValueInt):    
    event = models.ForeignKey('Event')    

class EventAttributeValueDecimal(AttributeValueDecimal):    
    event = models.ForeignKey('Event')    

class EventAttributeValueDate(AttributeValueDate):    
    event = models.ForeignKey('Event')    

class Event(EntityAbstract, RiskAppAware, LocationAware, HazardTypeAware, Exportable, Schedulable):        
    id = models.AutoField(primary_key=True)    
    code = models.CharField(max_length=25)
    hazard_type = models.ForeignKey(
        'Hazard',
        blank=False,
        null=False,
        unique=False,        
    )
    begin_date = models.DateField()            

    def get_attributes_saved(self):
        attributes_saved = []
        attributes_saved += EventAttributeValueVarchar.objects.filter(event=self)
        attributes_saved += EventAttributeValueText.objects.filter(event=self)
        attributes_saved += EventAttributeValueInt.objects.filter(event=self)
        attributes_saved += EventAttributeValueDecimal.objects.filter(event=self)
        attributes_saved += EventAttributeValueDate.objects.filter(event=self)
        return attributes_saved
    
    def get_extra_inline(self, data_type = None):
        attributes_saved = self.get_attributes_saved()
        return len(Event.get_attributes(data_type)) - len(attributes_saved)

class Phenomenon(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event)
    administrative_division = models.ForeignKey('AdministrativeDivision')
    begin_date = models.DateField()    

    class Meta:
        verbose_name_plural = 'Phenomena'

    def __unicode__(self):
        return u"id: {0} - date: {1} - location: {2}".format(self.event.code, self.begin_date, self.administrative_division.code)
