from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$',views.index),
    # url(r'^register',views.register) #Links refer to views to trigger NOT html files. The html file rendered is specified in the view function
    path('neworg/',views.registerOrg), #no '/' before name
    path('newuser/',views.registerUser),
    #Get user or org data to Edit in register.html
    path('getorg/<int:_id>',views.getOrg),
    path('getuser/<int:_id>',views.getUser),
    #APIs
    # path('editorg/<int:_id>',views.editOrg), #NO NEED FOR OTHER Urls, just do POST in 'getorg' like in 'neworg' (registerOrg)
    # path('edituser/<int:_id>',views.editUser),
    path('deleteorg/<int:_id>',views.deleteOrg),
    path('deleteuser/<int:_id>',views.deleteUser),
]
