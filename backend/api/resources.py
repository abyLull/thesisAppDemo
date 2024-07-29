from import_export import resources
from .models import Student,Destination

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class DestinationResource(resources.ModelResource):
    class Meta:
        model= Destination
