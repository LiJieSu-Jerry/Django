from django.contrib import admin

# Register your models here.
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	"""
	title=models.CharField(max_length=200)
	completed=models.BooleanField(default=False,blank=True,null=True)
	"""
	list_display=('title','completed')

admin.site.register(Task,TaskAdmin)