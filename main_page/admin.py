from django.contrib import admin
from .models import AllModels
# Register your models here.

admin.site.register(AllModels)


class ModelsAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_editable = ['description', 'image']
