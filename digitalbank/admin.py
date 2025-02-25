from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Mini Bank"
admin.site.site_title = "Mini Bank"
admin.site.site_url = "Mini Bank"

#We need to register the models
admin.site.register(CurrentBalance)
#admin.site.register(AddTransaction)

class AddTransactionAdmin(admin.ModelAdmin):
    list_display = [
    "current_balance",
        "username",
        "select_type",
        "enter_amount",
        "created_at"
    ]

    search_fields = ['select_type']
    list_filter = ['select_type']
    ordering = ['-select_type']
    #here we can define custom action functions and pass here to do bulk operations
    # actions = [make_credit, make_debit] --> we can pass functions (make_credit,make_debit) like this

admin.site.register(AddTransaction,AddTransactionAdmin)
