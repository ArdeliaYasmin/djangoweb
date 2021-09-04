from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['nama', 'dosen', 'sks', 'semester', 'tahun', 'ruang', 'deskripsi']
        widgets = {
            'nama'      : forms.TextInput(attrs={'class': 'form-control'}),
            'dosen'     : forms.TextInput(attrs={'class': 'form-control'}),
            'sks'       : forms.NumberInput(attrs={'class': 'form-control'}),
            'semester'  : forms.Select(attrs={'class': 'form-control'}),
            'tahun'     : forms.Select(attrs={'class': 'form-control'}),
            'ruang'     : forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi' : forms.Textarea(attrs={'class': 'form-control'}),
        }
