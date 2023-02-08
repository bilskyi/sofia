from django import forms


class ContactForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "ім'я"}), label=' ')
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'прізвище'}), label=' ')
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'телефонний номер'}), label=' ')
	