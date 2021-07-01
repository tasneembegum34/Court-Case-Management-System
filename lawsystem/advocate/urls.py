from django.urls import path

from . import views

urlpatterns=[

    path('home/',views.home,name='home'),
    path('advocateHome/',views.advocateHome,name='advocateHome'),
    path('advocateRegister/',views.advocateRegister),
    path('regSuccessful/',views.regSuccessful),

  
]