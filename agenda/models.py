from django.db import models

# classe do dono do animal
class Owners(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
    
# classe do animal em si
class Animals(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    dob = models.DateField(max_length=10, null=True)
    weight = models.FloatField(max_length=5, blank=True, null=True)
    is_alive = models.BooleanField()
    owner_id = models.ForeignKey(Owners, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

#########
# classe para as FICHAS
#########
class Records(models.Model):
    animal_id = models.ForeignKey(Animals, on_delete=models.SET_NULL, null=True)
    owner_id = models.ForeignKey(Owners, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Animal: {self.animal_id.name}"


# classe para consultas
class Appointments(models.Model):
    record_id = models.ForeignKey(Records, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=30, null=True)
    date = models.DateField(max_length=10, null=True)

    def __str__(self):
        return f"Consulta marcada para {self.animal_id.name}"
    
# classe para vacinas
class Vaccines(models.Model):
    type = models.CharField(max_length=4)
    last_date = models.DateField(max_length=10, null=True, blank=True)
    next_date = models.DateField(max_length=10, null=True, blank=True)
    lote = models.IntegerField()

    def __str__(self):
        return self.type

# classe para vacinas aplicadas
class TakenVaccines(models.Model):
    record_id = models.ForeignKey(Records, on_delete=models.SET_NULL, null=True, blank=True)
    vaccine_id = models.ForeignKey(Vaccines, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Vacina tomada por {self.animal_id.name}"
    
# classe para anamneses
class Anamnesis(models.Model):
    anamnese = models.TextField(max_length=3500)
    date = models.DateField(max_length=10, null=True)
    appointment_id = models.ForeignKey(Appointments, on_delete=models.SET_NULL, null=True, blank=True)
    vaccine_id = models.ForeignKey(Vaccines, on_delete=models.SET_NULL, null=True, blank=True)
    record_id = models.ForeignKey(Records, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Animal: {self.appointment_id.animal_id}"
    
# classe para prescrições
class Prescriptions(models.Model):
    prescription = models.TextField(max_length=2500)
    animal_id = models.ForeignKey(Animals, on_delete=models.SET_NULL, null=True, blank=True)
    appointment_id = models.ForeignKey(Appointments, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(max_length=10, null=True)
    record_id = models.ForeignKey(Records, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Prescrição feita para {self.animal_id.name}"
    
# classe para queixas 
class Complaints(models.Model):
    complaint = models.TextField(max_length=2000)
    appointment_id = models.ForeignKey(Appointments, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Queixa feita na consulta de id #{self.appointment_id}"