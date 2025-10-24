from django.db import models

# classe do dono do animal
class Owner(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    cpf = models.CharField(max_length=12)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
# classe do animal em si
class Animal(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    dob = models.DateField(max_length=10, null=True)
    weight = models.FloatField(max_length=5, blank=True, null=True)
    is_alive = models.BooleanField()
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True)
    pic = models.ImageField(upload_to='animals/', null=True, blank=True)

    def __str__(self):
        return f"ANIMAL: {self.name}. ID: #{self.id}"

#########
# classe para as FICHAS
#########
class Record(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"ANIMAL: {self.animal.name}. TUTOR: {self.owner.name}"


# classe para consultas
class Appointment(models.Model):
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=30, null=True)
    date = models.DateField(max_length=10, null=True)

    def __str__(self):
        return f"Consulta marcada. DATA: {self.date.strftime("%d/%m/%Y")}. ANIMAL: {self.record.animal.name} ID:{self.record.animal}"
    
# classe para vacinas
class Vaccine(models.Model):
    type = models.CharField(max_length=4)
    last_date = models.DateField(max_length=10, null=True, blank=True)
    next_date = models.DateField(max_length=10, null=True, blank=True)
    lote = models.IntegerField()

    def __str__(self):
        return f"Vacina: {self.type}"

# classe para vacinas aplicadas
class TakenVaccine(models.Model):
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Vacina: {self.vaccine.type}. ANIMAL: {self.record.animal.name} ID: #{self.record.animal}"
    
# classe para anamneses
class Anamnesis(models.Model):
    anamnese = models.TextField(max_length=3500)
    date = models.DateField(max_length=10, null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    takenVaccine = models.ForeignKey(TakenVaccine, on_delete=models.SET_NULL, null=True, blank=True)
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Anamnese salva. ANIMAL: {self.record.animal.name} ID: #{self.record.animal}"
    
# classe para prescrições
class Prescription(models.Model):
    prescription = models.TextField(max_length=2500)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(max_length=10, null=True)
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Prescrição feita. ANIMAL: {self.animal.name} ID: #{self.animal}"
    
# classe para queixas 
class Complaint(models.Model):
    complaint = models.TextField(max_length=2000)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Queixa registrada. ANIMAL: {self.appointment.record.animal.name} ID: #{self.appointment.record.animal.id}"