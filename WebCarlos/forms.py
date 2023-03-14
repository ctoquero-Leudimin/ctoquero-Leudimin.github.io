from django import forms

class Contacto(forms.Form):
	name = forms.CharField(label = "Nombre", max_length=100)
	email = forms.EmailField(label = "Correo electrónico", max_length=100)
	comment = forms.CharField(label = "Su comentario", widget=forms.Textarea)
