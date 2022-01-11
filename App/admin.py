from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)

admin.site.register(Status)

admin.site.register(Urgency)

admin.site.register(Sector)

@admin.register(Requestion)
class RequestionAdmin(admin.ModelAdmin):
    list_display = ("status", "title", "assigned", "applicant", "sector", "final_date", "urgency")
    list_filter = ("applicant", "status", )
    search_fields = ("title", )