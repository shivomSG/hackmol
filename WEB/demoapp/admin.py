from django.contrib import admin
from demoapp.models import patient
from demoapp.models import bed
from demoapp.models import patient_data
# Register your models here.

admin.site.register(patient)
admin.site.register(bed)
admin.site.register(patient_data)