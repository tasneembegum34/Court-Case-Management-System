from django.urls import path
from . import views
urlpatterns = [
    path('generateInvoice/',views.generateInvoice,name="generateInvoice" ),
]