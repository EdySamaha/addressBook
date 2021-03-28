from django.forms import ModelForm
# from .models import Organization,User
from register.models import User,Organization #NOT ..registerR

from django import forms

# Create the form class.
'''NOTE: forms are included in views to be rendered.
		the fields in each form include what inputs to render
'''
class Userid(ModelForm):
	class Meta:
		model = User
		fields = ['user_id']

class Orgid(ModelForm):
	class Meta:
		model = Organization
		fields = ['org_id']



