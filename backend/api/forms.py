from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Destination,Student
FACULTIES = [
    ('Wydział Administracji i Nauk Społecznych', 'Wydział Administracji i Nauk Społecznych'),
    ('Wydział Architektury', 'Wydział Architektury'),
]
class DestinationsForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['country', 'university', 'study_level_available','available_places', 'contract_code', 'year', 'comment']
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name', 'surname', 'year_of_study', 'study_level', 'contract_codes', 'year', 'comment', 'gpa', 'modified']
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    faculty = forms.ChoiceField(choices=FACULTIES, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "faculty", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.profile.faculty = self.cleaned_data["faculty"]
            user.profile.save()
        return user

class DataUploadForm(forms.Form):
    file = forms.FileField()
    year = forms.ChoiceField(choices=[(str(year), str(year)) for year in range(2000, 2051)])