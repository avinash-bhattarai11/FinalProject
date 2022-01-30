from django.contrib import admin
from .models import Product,Comment
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Product)
@admin.register(Comment)
class userdata(ImportExportModelAdmin):
    pass
