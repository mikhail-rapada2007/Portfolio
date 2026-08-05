from django.contrib import admin
from .models import Inquiry, Project, PersonalInfo, Testimony

# Register your models here.
admin.site.register(Project)
admin.site.register(PersonalInfo)
admin.site.register(Testimony)
admin.site.register(Inquiry)