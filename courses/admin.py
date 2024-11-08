from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'discount', 'image')

admin.site.register(Course, CourseAdmin)
