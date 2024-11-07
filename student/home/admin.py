from django.contrib import admin
from home.models import Student
# Register your models here.

def change_name(modeladmin, request, queryset):
    for student in queryset:
        student.name = student.name.upper()
        student.save()
change_name.short_description = "Change Name"
admin.site.register(Student)

