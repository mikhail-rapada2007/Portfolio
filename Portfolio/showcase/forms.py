from django import forms

class ProjectForm(forms.Form):
    project_name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    tech_stack = forms.CharField(required=False)
    link = forms.URLField(required=False)

class TestimonyForm(forms.Form):
    full_name = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

