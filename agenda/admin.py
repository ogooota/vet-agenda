from django.contrib import admin
from agenda.models import *

class AnimalAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'sex', 'dob', 'weight', 'is_alive',)
    search_fields = ('id', 'name')

class OwnerAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'phone')
    search_fields = ('id', 'name', 'phone')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_id')
    search_fields = tuple('animal_id')

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'last_date', 'next_date', 'lote')
    search_fields = ('id', 'type', 'lote')

class TakenVaccinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_id', 'vaccine_id')
    search_fields = ('id', 'animal_id')
    
class AnamneseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'anamnese')
    search_fields = tuple('id')

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'prescription')
    search_fields = tuple('id')

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment_id')
    search_fields = tuple('id')

admin.site.register(Animals, AnimalAdmin)
admin.site.register(Owners, OwnerAdmin)
admin.site.register(Appointments, AppointmentAdmin)
admin.site.register(Vaccines, VaccineAdmin)
admin.site.register(TakenVaccines, TakenVaccinesAdmin)
admin.site.register(Anamnesis, AnamneseAdmin)
admin.site.register(Prescriptions, PrescriptionAdmin)
admin.site.register(Complaints, ComplaintAdmin)
