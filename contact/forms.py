from django import forms

class ContactForm(forms.Form):
	name = forms.EmailField(required=True)
	from_email = forms.Email(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)