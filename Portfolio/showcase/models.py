from django.db import models

# Create your models here.

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.ManyToManyField(TechStack, blank=True)
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
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Testimony(models.Model):
    full_name = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.full_name

class Inquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
