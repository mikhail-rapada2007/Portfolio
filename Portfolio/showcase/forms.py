from django import forms
from .models import TechStack

class ProjectForm(forms.Form):
    project_name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    tech_stack = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    link = forms.URLField()

class TestimonyForm(forms.Form):
    full_name = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

class TechStackForm(forms.Form):
    name = forms.CharField()

class PersonalInfoForm(forms.Form):
    first_name = forms.CharField()
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField()
    summary = forms.CharField(widget=forms.Textarea)
    contact_number = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()