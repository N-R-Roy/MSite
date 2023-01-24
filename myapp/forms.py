from django import forms
from .models import PersonInfo


class PersonForm(forms.Form):
    name = forms.CharField(label="Name:", max_length=250)
    address = forms.CharField(label="Address:", max_length=250)
    age = forms.FloatField()


class AddForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = ['name', 'address', 'age']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = ['name', 'address', 'age']


class EmployeeForm(forms.Form):
    ename = forms.CharField(max_length=250)
    efile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

