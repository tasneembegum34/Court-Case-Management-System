from django.urls import path
from . import views
urlpatterns = [
    path('generateInvoice/',views.generateInvoice ,name="generateInvoice" ),
    path('invoice_data/',views.invoice_data ,name='invoice_data'),
    path('viewInvoice/',views.viewInvoice ,name='viewInvoice'),
    path('view_PDF/',views.view_PDF,name='view_PDF'),
    path('pdf/',views.generate_PDF,name='generate_PDF'),
]