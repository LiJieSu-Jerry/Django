from django.contrib import admin

from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	"""
	article_title=models.CharField()
	create_date=models.DateField()
	author=models.CharField()
	article_content=models.TextField()
	"""
	list_display=('post_title','pub_date','author')

admin.site.register(Post,PostAdmin)