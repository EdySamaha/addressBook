from django.conf.urls import url
from django.urls import path
from . import views

#MUST HAVE SAME NAME AS HTML TEMPLATES
urlpatterns = [
    # url(r'^$',views.index),
    # path('/user/<int:id>/',views.editUser), #No need since done in register and its path are referenced in addressbook.urls
    # path('/org/<int:id>/',views.editOrg)
]
