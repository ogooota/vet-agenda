from django.contrib import admin
from agenda.models import Animal, Owner

class AnimalAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'sex', 'dob', 'weight', 'is_alive',)
    search_fields = ('id', 'name')

class OwnerAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'phone')
    search_fields = ('id', 'name', 'phone')

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Owner, OwnerAdmin)