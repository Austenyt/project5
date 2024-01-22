from django.contrib import admin

from mainapp.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)

Admin.register(Subject)

Class SubjectAdmin(admin.ModelAdmin):

          List_display = (‘title’, ‘student’)

          List_filter = (‘student’)