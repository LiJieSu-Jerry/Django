from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import article
# Create your views here.

def Home(request):
	context={}
	context['article']=get_object_or_404(article)
	return render(request,'blog/home.html',context)

def Resume(request):
	return render(request,'blog/resume.html')




	"""
	template_name='blog/article_view.html'
	context_object_name='article_list'

	def get_queryset(self):
		return article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	"""