from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect #much better than return index(request) since No paramter collision
from .forms import RegisterOrg,RegisterUser,UsersFilter
from .models import User,Organization


orgselected=False
exists=False

def index(request): #get all data from dbs
	orgs= Organization.objects.order_by('orgname') #Organization.objects.all()
	users= User.objects.order_by('username') #User.objects.all()
	
	if request.method == 'GET': #Filter
		usersfilter= UsersFilter(request.GET, queryset=users)
		users= usersfilter.qs
	else:
		usersfilter= UsersFilter()
	return render(request, 'index.html', {'orgs':orgs, 'users':users, 'usersfilter':usersfilter})


#region User
def registerUser(request):
	global orgselected, exists
	orgselected=False
	exists=False
	if request.method == 'POST': #If data is sent => add to db and go back to index
		form = RegisterUser(request.POST)
		if form.is_valid():
			form.save()
			
			return redirect('/')

	else: #If no data sent (just visiting register page => render page)
		form = RegisterUser()
	return render(request, 'register.html', {'form': form, 'orgselected':orgselected, 'exists':exists})


def getUser(request, _id): #Get user page with info to edit
	try: #avoid invalid id error
		user = User.objects.get(user_id=_id)
		global orgselected, exists
		orgselected=False
		exists=True

		if request.method == 'POST': #Edit User (editUser)
			form = RegisterUser(request.POST, instance=user)
			if form.is_valid():
				form.save()
				return redirect('/')

		else: # See User data. Logically renders first since first accessed thorugh GET
			form = RegisterUser(instance=user)
			return render(request, 'register.html', {'form': form,'user':user, 'orgselected':orgselected, 'exists':exists})
	except:
		return redirect('/')


def deleteUser(request, _id): #API that renders back index
	try: #avoid invalid id error
		user = User.objects.get(user_id=_id)
		user.delete()
	except:
		pass
	return redirect('/')
#endregion

#region Org
def registerOrg(request):
	global orgselected, exists
	orgselected=True
	exists=False
	if request.method == 'POST': #If data is sent => add to db and go back to index
		form = RegisterOrg(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	else: #If no data sent (just visiting register page => render page)
		form = RegisterOrg()
	return render(request, 'register.html', {'form': form, 'orgselected':orgselected, 'exists':exists})


def getOrg(request, _id): #Get user page with info to edit
	try:
		org = Organization.objects.get(org_id=_id)
		global orgselected, exists
		orgselected=False
		exists=True

		if request.method == 'POST': #Edit Org (editOrg)
			form = RegisterOrg(request.POST, instance=org)
			if form.is_valid():
				form.save()
				return redirect('/')

		else: # See Org data. Logically renders first since first accessed thorugh GET
			form = RegisterOrg(instance=org)
			return render(request, 'register.html', {'form': form,'org':org, 'orgselected':orgselected, 'exists':exists})
	except:
		return redirect('/')


def deleteOrg(request, _id): #API that renders back index
	try:
		org = Organization.objects.get(org_id=_id)
		org.delete()
	except:
		pass
	return redirect('/')
#endregion
