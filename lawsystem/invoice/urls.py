from django.urls import path
from . import views
urlpatterns = [
    path('generateInvoice/',views.generateInvoice,name="generateInvoice" ),
    path('invoice_data/',views.invoice_data ,name='invoice_data'),
 

]