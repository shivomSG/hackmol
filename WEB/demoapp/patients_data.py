from turtle import textinput
from django import forms

class PatientForm(forms.Form):
    pt_name=forms.CharField(lable="Name", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    pt_age=forms.CharField(lable="Age", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    pt_gender=forms.CharField(lable="Gender", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    doctor=forms.CharField(lable="Doctor", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    date=forms.CharField(lable="Date", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
