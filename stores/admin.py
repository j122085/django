from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Store
from .models import MenuItem

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes',)
    inlines = (MenuItemInline,)

admin.site.register(Store, StoreAdmin)


# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price',)
#
# admin.site.register(MenuItem, MenuItemAdmin)