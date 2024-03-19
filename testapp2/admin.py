from django.contrib import admin
from testapp2.models import Book

# Register your models here.
class AdminBook(admin.ModelAdmin):
    list_display=["id","title","pages","price"]
admin.site.register(Book,AdminBook)
