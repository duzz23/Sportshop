from django.contrib import admin
from .models import Category, Equipment, Product, Excursion, DebugEquipment, ContactSent


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update')


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Equipment)
admin.site.register(Excursion)
admin.site.register(Product)
admin.site.register(DebugEquipment)

# DebugEquipment.objects.all().first().buy()

@admin.register(ContactSent)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', "date_burn", "telefon", "email", "description")
