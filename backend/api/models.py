
from django.db import models
from django.contrib.auth.models import User
APPLICATION_STATUS = [
    ('pending', 'Pending'),
    ('approved', 'Approved')
]
FACULTIES = [
    ('Wydział Administracji i Nauk Społecznych', 'Wydział Administracji i Nauk Społecznych'),
    ('Wydział Architektury', 'Wydział Architektury'),
    ('none', 'None'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=100, choices=FACULTIES, default='None')

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
class Destination(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinations")
    country = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    available_places = models.PositiveIntegerField()
    contract_code = models.CharField(max_length=25)
    student = models.ManyToManyField('Student', blank = True, null = True)
    year = models.CharField(max_length=4, default='2024')
    faculty = models.CharField(max_length=100, choices=FACULTIES, default='None')
    study_level_available = models.CharField(max_length=50, default='Not Provided')
    comment = models.TextField(default='None')
    #author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="destinations")

    def __str__(self):
        return f'{self.university} ({self.country})'

class Student(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    year_of_study = models.PositiveIntegerField()
    contract_codes = models.CharField(max_length=25)
    status = models.CharField(max_length=50, choices= APPLICATION_STATUS, default='Pending')
    year = models.CharField(max_length=4, default='2024')
    faculty = models.CharField(max_length=100, choices=FACULTIES, default='None')
    comment = models.TextField(default='None')
    study_level = models.CharField(max_length=20, default='Not Provided')
    gpa = models.FloatField(default=0, blank=True, null=True)  # Add GPA field
    MODIFIED_CHOICES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    ]
    modified = models.CharField(max_length=8, choices=MODIFIED_CHOICES, default='negative')  # Add Modified field
    def __str__(self):
        return f'{self.name} {self.surname}'