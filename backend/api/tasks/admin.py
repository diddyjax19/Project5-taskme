from django.contrib import admin

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','name','state']
    
admin.register(Task)