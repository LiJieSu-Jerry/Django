from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.views.decorators import csrf
from pathlib import Path
import datetime
import os
import json
import urllib.request

from .models import Post,Response,Visitor
# Create your views here.

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_FILES_DIR=os.path.join(BASE_DIR,'blog/static/')


def Home(request):
	visit_ip='73.134.227.100'#request.META['REMOTE_ADDR']
	context={}
	response=ipinfo(visit_ip)
	context['message']=last_time_visit_message(visit_ip)
	if is_new_traffic(visit_ip):
		record_traffic()
	context['ip']=visit_ip
	context['traffic']=get_traffic()
	
	context['post_list']=Post.objects.all()
	context['country']=response['country']
	context['region']=response['regionName']
	return render(request,'blog/home.html',context)

def Resume(request):
	return render(request,'blog/resume.html')

def Login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	username=request.POST.get('username','')
	password=request.POST.get()
	user=auth.authenticate(username=username,password=password)
	if user is not None and user.is_active:
		auth.login(request,user)
		return HttpResponseRedirect('/')
	else:
		return render(request,'blog/login.html',locals())

def Logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def User_check(request):
	return render(request,'blog/user_check.html')

def Response_create(request):
	if request.POST:
		context={}
		context['rlt']=request.POST['content']
		return render(request,'blog/form.html',context)
	return render(request,'blog/form.html')

def Response_receive_post(request):
	context={}
	if request.POST:
		context['rlt']=request.POST['content']
	return render(request,'blog/form.html',context)


def ipinfo(ip_address):
	request  = 'http://ip-api.com/json/'+ip_address
	req= urllib.request.Request(request)
	response= urllib.request.urlopen(req).read()
	json_response   = json.loads(response.decode('utf-8'))
	print(json_response['regionName'])
	return json_response



def is_new_traffic(visit_ip):
	try:
		now_visitor=Visitor.objects.get(ip_address=visit_ip)
	except:
		now_visitor=None
	now_time=timezone.now()
	if now_visitor==None:
		new_visitor=Visitor(ip_address=visit_ip,visit_time=now_time)
		new_visitor.save()
		return True
	else:
		if now_time-now_visitor.visit_time>=datetime.timedelta(days=1):
			Visitor.objects.filter(ip_address=visit_ip).update(visit_time=now_time)
			return True
		else:
			return False

def last_time_visit_message(visit_ip):
	try:
		now_visitor=Visitor.objects.get(ip_address=visit_ip)
	except:
		now_visitor=None
	if now_visitor==None:
		return "This is the first time you visit this website."
	else:
		a=now_visitor.visit_time.date()
		#date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
		message="Hello, the time of your last visit is {}".format(a)
		return message


def record_traffic():
	file_path=os.path.join(STATIC_FILES_DIR,"count.dat")
	with open(file_path,'r') as f:
		count_text=f.readline()
	with open(file_path,'w') as f:
		if count_text=="":
			f.write(str(0))
		else:
			count=int(count_text)
			f.write(str(count+1))
		f.close()

def get_traffic():
	file_path=os.path.join(STATIC_FILES_DIR,"count.dat")
	with open(file_path,'r') as f:
		count_text=f.readline()
	return count_text



    

"""
{'status': 'success', 
'country': 'United States', 
'countryCode': 'US', 
'region': 'MD', 
'regionName': 'Maryland', 
'city': 'Bethesda', 
'zip': '20814', 
'lat': 39.0016, 
'lon': -77.0961, 
'timezone': 'America/New_York', 
'isp': 'Comcast Cable Communications, LLC', 
'org': 'Comcast Cable Communications, Inc.', 
'as': 'AS7922 Comcast Cable Communications, LLC', 
'query': '73.134.227.105'}
	"""


"""
	def get_queryset(self):
		return article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	"""