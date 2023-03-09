from django.contrib import admin
from .models import Filiaire, Student, Program


@admin.register(Filiaire)
class FiliaireAdmin(admin.ModelAdmin):
    list_display = ['filiaire']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['promotion', 'photo', 'start_stage', 'end_stage', 'sex']
    list_per_page = 10
    list_editable = ['photo', 'start_stage', 'end_stage', 'sex']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['programme' , 'date']
    search_fields = ['programme']
    list_per_page = 10
    list_editable = ['date']