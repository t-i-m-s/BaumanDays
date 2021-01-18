from django.contrib import admin

# Register your models here.
from .models import TeacherRating, Comment

admin.site.register(TeacherRating)
admin.site.register(Comment)