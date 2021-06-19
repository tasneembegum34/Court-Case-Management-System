from django.contrib import admin
from advocate.models import advocateAccounts
from client.models import clientAccounts,sectionNoDetails
# Register your models here.

class AdvocateAccountsAdmin(admin.ModelAdmin):
    pass


admin.site.register(advocateAccounts,AdvocateAccountsAdmin)
admin.site.register(clientAccounts)
admin.site.register(sectionNoDetails)