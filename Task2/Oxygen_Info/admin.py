from django.contrib import admin
from .models import Oxygen
# Register your models here.

@admin.register(Oxygen)
class OxygenAdmin(admin.ModelAdmin):
    list_display = ['id','Address','Business_Name','Person_Name','Contact_No','Verify_Status','TimeStamp']