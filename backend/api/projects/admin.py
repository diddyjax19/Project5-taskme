from django.contrib import admin

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','name','start_date','end_date']