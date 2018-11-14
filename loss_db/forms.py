from django.forms import BaseInlineFormSet
from loss_db.models import Event
from loss_db.models.eav_attribute import data_types


class EventAttributeInlineFormSet(BaseInlineFormSet):        
    def __init__(self, *args, **kwargs): 
        data_type = None        
        for t in data_types:
            if t[0] in kwargs['prefix']:                    
                data_type = t[0]
                break
        if data_type:        
            event_attributes = Event.get_attributes(data_type)         
            if event_attributes:
                kwargs['initial'] = []            
                for a in event_attributes:
                    if a not in kwargs['queryset']:
                        kwargs['initial'].append({'attribute': a})                         
                        
        super(EventAttributeInlineFormSet, self).__init__(*args, **kwargs)