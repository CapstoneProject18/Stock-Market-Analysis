from django.contrib import admin

# Register your models here.
from testapp.models import Note


class NoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Note, NoteAdmin)