from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Destination,Student
# Register your models here.
admin.site.register(Destination)
class DestinationAdmin(ImportExportModelAdmin):
    list_display = ('country','university','available_places','contract_code','student','author')
admin.site.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('name','surname','year_of_study','status','contract_codes','author')