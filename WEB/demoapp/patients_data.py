from turtle import textinput
from django import forms
DOCTOR=[('d1','D1'),
        ('d2','D2'),
        ('d3','D3'),
        ('d4','D4')]
GENDER=[('male','Male'),('female','Female'),('other','Other')]

class PatientForm(forms.Form):
    pt_name=forms.CharField(label='Patient Name')
    pt_age=forms.IntegerField(label='Age')
    pt_gender=forms.CharField(label='Gender',widget=forms.Select(choices=GENDER))
    doctor=forms.CharField(label='Doctor', widget=forms.Select(choices=DOCTOR))
    date=forms.DateField()
