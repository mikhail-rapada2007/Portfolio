from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(blank=True, null=True, max_length=300, help_text="e.g. Python, Django, SQLite")
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"