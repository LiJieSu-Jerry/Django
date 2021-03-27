from django.contrib import admin

from .models import article
# Register your models here.
class articleAdmin(admin.ModelAdmin):
	"""
	article_title=models.CharField()
	create_date=models.DateField()
	author=models.CharField()
	article_content=models.TextField()
	"""
	list_display=('article_title','pub_date','author')

admin.site.register(article,articleAdmin)