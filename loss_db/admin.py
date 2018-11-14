# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import nested_admin

# Register your models here.
from loss_db.models import (AnalysisType, AssetCategory, Asset, AssetItem, MarketValue, DamageType, DamageTypeValue,
                                DamageAssessment, DamageAssessmentValue, EavAttribute,
                                Event, Phenomenon, EventAttributeValueVarchar, EventAttributeValueText,
                                EventAttributeValueInt, EventAttributeValueDecimal, EventAttributeValueDate,
                                Hazard, AdministrativeDivision, Location,
                                Owner, SendaiTarget, SendaiIndicator)
from loss_db.forms import EventAttributeInlineFormSet


admin.site.site_header = 'Risk Data Hub / Loss Database demo'

class EventAttributeValueVarcharInline(admin.StackedInline):
    def get_extra(self, request, obj=None, **kwargs):        
        return obj.get_extra_inline('varchar')        
    
    model = EventAttributeValueVarchar    
    readonly_fields = ('data_type',)
    formset = EventAttributeInlineFormSet        
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(EventAttributeValueVarcharInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'attribute':
            field.queryset = field.queryset.filter(data_type='varchar')
        return field

class EventAttributeValueTextInline(admin.StackedInline):
    def get_extra(self, request, obj=None, **kwargs):        
        return obj.get_extra_inline('text')        
    
    model = EventAttributeValueText
    readonly_fields = ('data_type',)
    formset = EventAttributeInlineFormSet        
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(EventAttributeValueTextInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'attribute':
            field.queryset = field.queryset.filter(data_type='text')
        return field

class EventAttributeValueIntInline(admin.StackedInline):
    def get_extra(self, request, obj=None, **kwargs):        
        return obj.get_extra_inline('int')        
    
    model = EventAttributeValueInt
    readonly_fields = ('data_type',)
    formset = EventAttributeInlineFormSet        
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(EventAttributeValueIntInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'attribute':
            field.queryset = field.queryset.filter(data_type='int')
        return field

class EventAttributeValueDecimalInline(admin.StackedInline):
    def get_extra(self, request, obj=None, **kwargs):        
        return obj.get_extra_inline('decimal')        
    
    model = EventAttributeValueDecimal
    readonly_fields = ('data_type',)
    formset = EventAttributeInlineFormSet        
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(EventAttributeValueDecimalInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'attribute':
            field.queryset = field.queryset.filter(data_type='decimal')
        return field

class EventAttributeValueDateInline(admin.StackedInline):
    def get_extra(self, request, obj=None, **kwargs):        
        return obj.get_extra_inline('date')        
    
    model = EventAttributeValueDate
    readonly_fields = ('data_type',)
    formset = EventAttributeInlineFormSet        
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(EventAttributeValueDateInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'attribute':
            field.queryset = field.queryset.filter(data_type='date')
        return field

class MarketValueInline(nested_admin.NestedStackedInline):
    model = MarketValue
    extra = 0

class AssetItemInline(nested_admin.NestedStackedInline):
    model = AssetItem
    extra = 1
    inlines = [MarketValueInline]

class SendaiIndicatorInline(admin.StackedInline):
    model = SendaiIndicator
    extra = 1

class DamageTypeValueInline(admin.TabularInline):
    model = DamageTypeValue
    extra = 2

class PhenomenonInline(admin.StackedInline):
    model = Phenomenon
    extra = 1

class AdministrativeDivisionAdmin(admin.ModelAdmin):
    model = AdministrativeDivision
    list_display_links = ('id',)
    list_display = ('id', 'code', 'name',)

class AnalysisTypeAdmin(admin.ModelAdmin):
    model = AnalysisType
    list_display_links = ('id',)
    list_display = ('id', 'name', 'title', 'scope',)

class AssetCategoryAdmin(admin.ModelAdmin):
    model = AssetCategory
    list_display_links = ('id',)
    list_display = ('id', 'name',)

class AssetAdmin(nested_admin.NestedModelAdmin):
    model = Asset
    list_display_links = ('id',)
    list_display = ('id', 'name',)
    readonly_fields = ('_entity_type',)
    inlines = [AssetItemInline]

class DamageTypeAdmin(admin.ModelAdmin):
    model = DamageType
    list_display_links = ('id',)
    list_display = ('id', 'name', 'abstract', 'unit',)
    inlines = [DamageTypeValueInline]

class DamageAssessmentAdmin(admin.ModelAdmin):
    model = DamageAssessment
    list_display_links = ('id',)
    list_display = ('id', 'name', 'analysis_type', 'unit_of_measure',)
    inlines = [DamageTypeValueInline]

class DamageAssessmentValueAdmin(admin.ModelAdmin):
    model = DamageAssessmentValue
    list_display_links = ('id',)
    list_display = ('id', 'damage_assessment', 'phenomenon', 'damage_type_value_1', 'damage_type_value_2', 'item', 'value',)    

class EavAttributeAdmin(admin.ModelAdmin):
    model = EavAttribute
    list_display_links = ('id',)
    list_display = ('id', 'code', 'name', 'entity_type',)

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display_links = ('id',)
    list_display = ('id', 'code', 'begin_date',)
    readonly_fields = ('_entity_type',)
    inlines = [EventAttributeValueVarcharInline, EventAttributeValueTextInline, EventAttributeValueIntInline, EventAttributeValueDecimalInline, EventAttributeValueDateInline, PhenomenonInline]    

class HazardAdmin(admin.ModelAdmin):
    model = Hazard
    list_display_links = ('id',)
    list_display = ('id', 'mnemonic', 'title',)

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display_links = ('id',)
    list_display = ('id', 'location_type', 'address', 'lat', 'lon', 'administrative_division',)

class OwnerAdmin(admin.ModelAdmin):
    model = Owner
    list_display_links = ('id',)
    list_display = ('id', 'name',)

class SendaiTargetAdmin(admin.ModelAdmin):
    model = SendaiTarget
    list_display_links = ('id',)
    list_display = ('id', 'name', 'description',)
    inlines = [SendaiIndicatorInline]


admin.site.register(AdministrativeDivision, AdministrativeDivisionAdmin)
admin.site.register(AnalysisType, AnalysisTypeAdmin)
admin.site.register(AssetCategory, AssetCategoryAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(DamageType, DamageTypeAdmin)
admin.site.register(DamageAssessment, DamageAssessmentAdmin)
admin.site.register(DamageAssessmentValue, DamageAssessmentValueAdmin)
admin.site.register(EavAttribute, EavAttributeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Hazard, HazardAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(SendaiTarget, SendaiTargetAdmin)