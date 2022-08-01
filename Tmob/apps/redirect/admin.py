from django.contrib import admin

# Register your models here.
from apps.redirect.models import Redirect

class RedirectAdmin(admin.ModelAdmin):
    search_fields = [ "key","url",]
    list_display= [ "pk","key","url","active","created_at","updated_at"]
    list_filter = ["active"]

admin.site.register(Redirect,RedirectAdmin)