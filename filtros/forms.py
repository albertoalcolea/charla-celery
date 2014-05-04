from django import forms

class UploadFileForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    foto  = forms.FileField()
