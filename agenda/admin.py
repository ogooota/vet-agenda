from django.contrib import admin
from agenda.models import *



# vaccines

class TakenVaccineAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_id', 'vaccine_id')
    search_fields = ('id', 'record_id')

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'last_date', 'next_date', 'lote')
    search_fields = ('id', 'type', 'lote')

# all origin tables are found starting down and going up
# eg: you need an owner to have an animal,
#     you need a record to have an appointment... (goes on)

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'prescription')
    search_fields = tuple('id')

class AnamneseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'anamnese')
    search_fields = tuple('id')

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment_id')
    search_fields = tuple('id')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_id')
    search_fields = tuple('record_id')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal_id', 'owner_id')
    search_fields = ('id', 'animal_id', 'owner_id')
    
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'dob', 'weight', 'is_alive',)
    search_fields = ('id', 'name')

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    search_fields = ('id', 'name', 'phone')


# registrations for admin

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(TakenVaccine, TakenVaccineAdmin)
admin.site.register(Anamnesis, AnamneseAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Record, RecordAdmin)