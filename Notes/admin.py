from django.contrib import admin
from .models import UserNotes
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)


admin.site.register(UserNotes,NotesAdmin)
