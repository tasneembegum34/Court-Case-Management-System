from django.urls import path

from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('clientHome/',views.clientHome,name='clientHome'),
     path('clientRegister/',views.clientRegister),
    path('search/',views.searchSection,name='search-sections'),
    path('hireAdvocates/',views.hireAdvocates,name='hire'),
    path('caseStatus/',views.caseStatus,name='caseStatus'),

]