from django.urls import path

from . import views

urlpatterns=[

    path('hireAdvocates/',views.hireAdvocates),
    path('criminalAd/',views.criminalAd,name='criminalAd'),
    path('civilAd/',views.civilAd,name='civilAd'),
    path('firms/',views.firms,name='firms'),
    path('MyAdList/',views.MyAdList,name="MyAdList"),
    path('MyClientList/',views.MyClientList ),
    path('clientRequests/',views.clientRequests,name="clientRequests" ),
    path('confirmedAds/',views.confirmedAds ,name="confirmedAds" ),
    path('suggestingAds/',views.suggestingAds,name="suggestingAds" ),

]