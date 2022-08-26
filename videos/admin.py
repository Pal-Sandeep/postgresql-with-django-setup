from django.contrib import admin
from . import models
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields= ['release_year','title','length']

    search_fields = ['title','length']

    list_filter = ['release_year','length','title']

    list_display = ['title','release_year','length']

    list_editable = ['length']
 


admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)