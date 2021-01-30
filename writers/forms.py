'''
from django import forms
from django.contrib.auth.models import User, Writer
from django .contrib.auth.forms import UserCreationForm
from django.db import transaction

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = [ 'first_name', 'last_name','username', 'email', 'password1', 'password2']

		witdgets ={
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'password1': forms.TextInput(attrs={'class': 'form-control'}),
			'password2': forms.TextInput(attrs={'class': 'form-control'}),
		}

class ClientSignUpForm(UserRegisterForm):
    class Meta(UserRegisterForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        if commit:
            user.save()
        return user

class WriterSignUpForm(UserRegisterForm):
    class Meta(UserRegisterForm.Meta):
		interests = forms.ModelMultipleChoiceField(
			queryset=Speciality.objects.all(),
			widget=forms.CheckboxSelectMultiple,
			required=True
		)
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_writer = True
        user.save()
        writer = Writer.objects.create(user=user)
        writer.interests.add(*self.cleaned_data.get('interests'))
        return user
'''