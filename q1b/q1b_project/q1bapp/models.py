from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','username']

    USER_TYPE_CHOICES = (
        ('D', 'Doctor'),
        ('S', 'Staff'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13,null=True,blank=True)
    email = models.EmailField(null=True,blank=True,unique=True)
    address = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=155,null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    designation = models.CharField(max_length=155,null=True,blank=True)




class Patient(models.Model):
    registration_id = models.CharField(max_length=255, null=True, blank=True)
    firstname_patient_name = models.CharField(max_length=255, null=True, blank=True)
    secondname_patient_name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    rec_no = models.IntegerField()
    is_active = models.BooleanField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    mob_no = models.CharField(max_length=13,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    state = models.CharField(max_length=13,null=True,blank=True)
    city = models.CharField(max_length=13,null=True,blank=True)
    locality = models.CharField(max_length=13,null=True,blank=True)
    address = models.CharField(max_length=13,null=True,blank=True)
    dob = models.CharField(max_length=13,null=True,blank=True)
    age = models.IntegerField()
    second_phone_number = models.IntegerField()
    guardian_name = models.CharField(max_length=13,null=True,blank=True)
    op_number = models.IntegerField()
    passport_number = models.CharField(max_length=13,null=True,blank=True)
    discharge_date =  models.DateTimeField(auto_now_add=True)
    gender =  models.CharField(max_length=13,null=True,blank=True)
    country = models.CharField(max_length=13,null=True,blank=True)
    Medicalhistory = models.CharField(max_length=255,null=True,blank=True)
    zip = models.CharField(max_length=13,null=True,blank=True)
    bloodgroup = models.CharField(max_length=13,null=True,blank=True)
    remarks = models.CharField(max_length=13,null=True,blank=True)
    fee = models.CharField(max_length=13,null=True,blank=True)
    payment = models.CharField(max_length=13,null=True,blank=True)
    conditions = models.CharField(max_length=13,null=True,blank=True)
    pregnant = models.CharField(max_length=13,null=True,blank=True)
    occupation = models.CharField(max_length=13,null=True,blank=True)
    remarks = models.CharField(max_length=13,null=True,blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    specialization = models.CharField(max_length=13,null=True,blank=True)
    # doctor = models.CharField(max_length=13,null=True,blank=True)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    referredBy = models.CharField(max_length=13,null=True,blank=True)
    patient_group = models.CharField(max_length=13,null=True,blank=True)
    register_method = models.CharField(max_length=13,null=True,blank=True)

class Medicine(models.Model):

    TIME_CHOICES = (
        ('AM', 'AM'),
        ('NOON', 'NOON'),
        ('PM', 'PM'),
    )
    MEDICINE_CHOICES = (
        ('Before Meal', 'Before Meal'),
        ('After Meal', 'After Meal'),
    )

    name = models.CharField(max_length=13,null=True,blank=True)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='medicines')
    time = models.CharField(max_length=100, choices=TIME_CHOICES)
    medicine_choice = models.CharField(max_length=100, choices=MEDICINE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class MedicineList(models.Model):

    name = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




# class Appointment(models.Model):
#     pateint_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
#     is_active = models.BooleanField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     treatment = models.CharField(max_length=13,null=True,blank=True)
#     notes = models.CharField(max_length=343,null=True,blank=True)


class Eventappointment(models.Model):
    title = models.CharField(max_length=200)
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    treatment = models.CharField(max_length=130,null=True,blank=True)
    notes = models.CharField(max_length=343,null=True,blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    

