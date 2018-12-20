from django.contrib import admin
from .models import Companies
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Companies)
class CompanyAdmin(ImportExportModelAdmin):
    pass
# Need to register my Company so it shows up in the admin
# admin.site.register(Company)