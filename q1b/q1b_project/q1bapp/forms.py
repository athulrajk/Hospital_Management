#forms.py
from django import forms
from q1bapp.models import *
from .models import Eventappointment,Patient,Medicine


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        
class EventForm(forms.ModelForm):
    class Meta:
        model = Eventappointment
        fields = ['title', 'start_time', 'end_time', 'description','patient_id','treatment','notes','doctor']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['doctor', 'patient', 'name', 'time', 'medicine_choice']