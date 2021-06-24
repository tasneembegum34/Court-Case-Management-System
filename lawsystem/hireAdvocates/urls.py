from django.urls import path

from . import views

urlpatterns=[

    path('hireAdvocates/',views.hireAdvocates),
    path('criminalAd/',views.criminalAd,name='criminalAd'),
    path('civilAd/',views.civilAd),
    path('firms/',views.firms),
    path('MyAdList/',views.MyAdList,name="MyAdList"),
    path('MyClientList/',views.MyClientList ),
    path('clientRequests/',views.clientRequests,name="clientRequests" ),

]