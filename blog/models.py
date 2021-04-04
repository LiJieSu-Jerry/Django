from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	post_title=models.CharField(max_length=100)
	pub_date=models.DateTimeField('date published',auto_now_add=True)
	author=models.CharField(max_length=50)
	post_content=models.TextField()

	def __str__(self):
		return self.article_title

class Response(models.Model):
	pub_date=models.DateTimeField('date published',auto_now_add=True)
	response_content=models.TextField()
	reponsed_post=models.ForeignKey(Post,on_delete=models.CASCADE,)

class Visitor(models.Model):
	ip_address = models.GenericIPAddressField()
	visit_time=models.DateTimeField('date visited')

