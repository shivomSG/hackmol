from turtle import textinput
from django import forms
DOCTOR=[('d1','D1'),
        ('d2','D2'),
        ('d3','D3'),
        ('d4','D4')]
GENDER=[('male','Male'),('female','Female'),('other','Other')]

class PatientForm(forms.Form):
    pt_name=forms.CharField(required=False,label="Patient Name", widget=forms.TextInput(attrs={'class':"form-control"}))
    pt_age=forms.IntegerField(required=False, label="Age", widget=forms.TextInput(attrs={'class':"form-control"}))
    pt_gender=forms.CharField(label='Gender',widget=forms.Select(choices=GENDER))
    doctor=forms.CharField(label='Doctor', widget=forms.Select(choices=DOCTOR))
    date=forms.DateField()
