from django.urls import path

from . import views

urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('advocateSettings/',views.advocateSettings ,name='advocateSettings'),
    path('clientSettings/',views.clientSettings ,name='clientSettings'),
]