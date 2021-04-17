from django.contrib import admin

from .models import Snippet
# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
	"""
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
	"""
	list_display=('created','title','code','linenos','language','style')

admin.site.register(Snippet,SnippetAdmin)