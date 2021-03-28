from django.forms import ModelForm
from .models import Organization,User
from django import forms 
# from rest_framework import serializers #Serializers for APIs

# Create the form class.
'''NOTE: forms are included in views to be rendered.
		the fields in each form include what inputs to render
'''

class RegisterUser(ModelForm):
	class Meta:
		model = User	
		fields = ['username', 'email','phone','org_id']

class RegisterOrg(ModelForm):
	class Meta:
		model = Organization	
		fields = ['orgname', 'email','phone']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class OrganizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Organization
#         fields = '__all__'

