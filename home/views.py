from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .forms import Userid,Orgid
from register.models import User,Organization #NOT ..register

#NO NEED. ALL DONE IN register.views
# def index(request): #get all data from dbs
#     orgs=Organization.objects.all()
#     users=User.objects.all()
#     return render(request, 'index.html', {'orgs':orgs, 'users':users})

#In register.views
# def editUser(request, id):
#     return render(request,'register.html')

# def editOrg(request, id):
#     return render(request,'register.html')