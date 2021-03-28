from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$',views.index),
    # url(r'^register',views.register)
    path('neworg/',views.registerOrg), #no '/' before name
    path('newuser/',views.registerUser),
    # path('Users', views.UserViewSet.as_view({
    #     'get': 'getall',
    #     'post': 'register'
    # })),
    # path('Users/<str:pk>', views.UserViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),

    #  path('Organizations', views.OrganizationViewSet.as_view({
    #     'get': 'getall',
    #     'post': 'register'
    # })),
    # path('Organizations/<str:pk>', views.OrganizationViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
]
