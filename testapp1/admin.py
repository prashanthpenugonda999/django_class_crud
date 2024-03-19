from django.contrib import admin
from testapp1.models import student

# Register your models here.
class admin_view(admin.ModelAdmin):
    list_display=['id','name','age']

admin.site.register(student,admin_view)
