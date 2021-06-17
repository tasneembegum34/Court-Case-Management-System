from django.urls import path

from . import views

urlpatterns=[

    path('hireAdvocates/',views.hireAdvocates),
    path('criminalAd/',views.criminalAd),
    path('civilAd/',views.civilAd),
    path('commonAd/',views.commonAd),
    path('statutoryAd/',views.statutoryAd),
    path('firms/',views.firms),


]