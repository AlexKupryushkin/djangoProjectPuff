from django.contrib import admin
from .models import *


class SoftAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'type')
    list_filter = ('type',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Divan, SoftAdmin)
admin.site.register(Orders)
admin.site.register(Type)
