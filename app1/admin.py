from django.contrib import admin
from .models import Product, Customer, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display =['link',]

admin.site.register(Contact)






#admin.site.register(Product)



