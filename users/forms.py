from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class NewUserForm(UserCreationForm):
	'''User form with explicitly checking email in overriding save function'''
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("name", "email", "password1", "password2", "is_staff")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user