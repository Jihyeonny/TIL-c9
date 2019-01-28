from django.contrib import admin
from .models import Migrate
# Register your models here.
class MigrateAdmin(admin.ModelAdmin):
    list_display=('name','email','birthday','age',)
    
admin.site.register(Migrate, MigrateAdmin)

