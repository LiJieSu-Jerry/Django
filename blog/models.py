from django.db import models
from django.utils import timezone

# Create your models here.
class article(models.Model):
	article_title=models.CharField(max_length=100)
	pub_date=models.DateTimeField('date published',default=timezone.now())
	author=models.CharField(max_length=50)
	article_content=models.TextField()

	def __str__(self):
		return self.article_title