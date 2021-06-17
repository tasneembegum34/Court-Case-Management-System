from django.urls import path

from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('clientHome/',views.clientHome),
     path('clientRegister/',views.clientRegister,name='client-Home'),
    path('search/',views.searchSection,name='search-sections'),
    path('hireAdvocates/',views.hireAdvocates),

]