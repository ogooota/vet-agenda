from django.db import models

# classe do dono do animal
class Owner(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
    
# classe do animal em si
class Animal(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    dob = models.DateField(max_length=10, null=True)
    weight = models.FloatField(max_length=5, blank=True, null=True)
    is_alive = models.BooleanField()
    owner_id = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# classe para consultas
class Appointment(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=30, null=True)
    date = models.DateField(max_length=10, null=True)

    def __str__(self):
        return f"Consulta marcada para {self.animal_id.name}"
    
# classe para vacinas
class Vaccine(models.Model):
    type = models.CharField(max_length=4)
    last_date = models.DateField(max_length=10, null=True, blank=True)
    next_date = models.DateField(max_length=10, null=True, blank=True)
    lote = models.IntegerField()

    def __str__(self):
        return self.type

# classe para vacinas aplicadas
class TakenVaccines(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Vacina tomada por {self.animal_id.name}"
    
# classe para anamneses
class Anamnese(models.Model):
    anamnese = models.TextField(max_length=3500)
    date = models.DateField(max_length=10, null=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Animal: {self.appointment_id.animal_id}"
    
# classe para prescrições
class Prescription(models.Model):
    prescription = models.TextField(max_length=2500)
    animal_id = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(max_length=10, null=True)

    def __str__(self):
        return f"Prescrição feita para {self.animal_id.name}"
    
# classe para queixas 
class Complaint(models.Model):
    complaint = models.TextField(max_length=2000)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Queixa feita na consulta de id #{self.appointment_id}"    