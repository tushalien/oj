from django.contrib import admin
from . import models

# Register your models here.
class SubmissionsAdmin(admin.ModelAdmin):
    list_display = ['rid', 'name','code','error','output'] 

class RunsAdmin(admin.ModelAdmin):
    list_display = ['rid', 'pid','tid','language','time','result','submittime'] 


admin.site.register(models.Submissions, SubmissionsAdmin)

#admin.site.register(models.Submissions)
admin.site.register(models.Runs,RunsAdmin)
