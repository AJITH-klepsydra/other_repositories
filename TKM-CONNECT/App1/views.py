from django.shortcuts import render,redirect,get_object_or_404
from django.forms.models import model_to_dict
#auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from utils.forms import UserCreationForm,UserLoginForm
from .forms import *
from .models import *
from .models import Profile as UserProfile
from utils.models import Member
from django.http import HttpResponse
from django.http import JsonResponse
def Signup(request,*args,**kwargs):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('profedit')
	return render(request, 'accounts/signup.html',{'form':form})

@login_required(login_url='/login/')
def Job_Submits(request):
	if not request.user.is_complete:
		return redirect('profedit')
	print(request.user.is_alumni)
	if request.user.is_alumni:
		form = job_post_form()
		if request.method=='POST':
			Job_post.objects.all().create(
				alumni=request.user,
				title=request.POST['title'],
				description=request.POST['description'],
				image=request.POST['image'])
			return redirect('home')
		return render(request,'jobsubmit/job_submit.html',{'form':form})
	else:
		return redirect('home')
#@login_required(login_url='/login/')
def Profile(request,val):
	if not request.user.is_complete:
		return redirect('profedit')
	if request.method=='POST':
		print(request.POST)
	try:
		username=str(request.user.username)
		a=Member.objects.all().get(pk=val)
		cnt=a.profile.Projects.all().count()
		projects = a.profile.Projects.all() 
		return render(request, "profile/profile.html",{'user':a,'count':cnt,'projects':projects,'username':username})
	except Exception as e:
		print(e)
		return redirect('home')
@login_required(login_url='/login/')
def Home(request):
	if not request.user.is_complete:
		return redirect('profedit')

	jobs=Job_post.objects.all()
	if request.method=="POST":
		print("hi")

		user2=Member.objects.get(username=request.POST['alumni'])
		job=Job_post.objects.get(title=request.POST['title'])
		Request.objects.all().create(user=request.user,alumni=user2,job=job)
		return redirect('profile',val=user2.id)
	blogs=Blog.objects.all().exclude(author=request.user)
	req_list=Request.objects.all().filter(alumni=request.user)
	return render(request, 'home/home.html',{'jobs':jobs,'requests':req_list,'blogs':blogs})
def Login(request,*args,**kwargs):

	if request.user.is_authenticated:
		return redirect('home')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user_obj=form.cleaned_data.get('user_obj')
		login(request, user_obj)
		return redirect('home')
	return render(request, "accounts/login.html",{'form':form,})
def Logout(request):
	logout(request)
	return redirect('login')
@login_required(login_url='/login/')
def AddProject(request):
	if not request.user.is_complete:
		return redirect('profedit')
	form = ProjectForm()
	if request.method=="POST":
		print (request.POST)
		a=Project.objects.all().create(user=request.user,title=request.POST['title'],description=request.POST['description'],link=request.POST['link'])
		request.user.profile.Projects.add(a)
		return render(request, 'profile/addproj.html',{'form':form,'button':"Add again"})
	return render(request, 'profile/addproj.html',{'form':form,'button':"Add"})
@login_required(login_url='/login/')
def Editprofile(request):

	form = ProfileForm()
	if request.method=='POST':
			UserProfile.objects.all().create(
				user=request.user,
				Dob=request.POST['Dob'],
				department=request.POST['department'],
				semester=request.POST['semester'],
				insta_id=request.POST['insta_id'],
				linkedin=request.POST['linkedin'],
				nick_name=request.POST['nick_name'],
				image=request.POST['image'],

				)
			request.user.is_complete=True
			request.user.save()
			return redirect('home')
	return render(request, 'profile/profedit.html',{'form':form})
@login_required(login_url='/login/')
def AddBlog(request):
	if not request.user.is_complete:
		return redirect('profedit')
	form = BlogForm()
	if request.method=="POST":
		print (request.POST)
		a=Blog.objects.all().create(author=request.user,title=request.POST['title'],description=request.POST['description'],link=request.POST['link'])
		
		return redirect('home')
	return render(request, 'profile/addblog.html',{'form':form,'button':"Add"})
@login_required(login_url='/login/')
def Chat(request):
	return render(request, 'chat/room.html')
def get_messages(request):

	messages=Message.objects.all().order_by('date_time')
	contxt={}
	k=0
	for msg in messages:
		if msg.sender.is_alumni:
			case="border:4px solid yellow"
		else:
			case="border:0px solid yellow"
		if msg.sender.username == request.user.username:
			var="sent"
		else:
			var="replies"
		contxt[k]={'message':msg.message,
					'sender':msg.sender.username,
					'image':msg.sender.profile.image,
					'group':msg.group,
					'class':var,
					'case':case}
		k+=1
	return contxt

def Savemsg(request):
	if request.is_ajax and request.method=="GET":
			print("What")
			Message.objects.all().create(sender=request.user,group="global",message=request.GET['message'])
			return JsonResponse(get_messages(request))
def Showmsg(request):
	if request.is_ajax and request.method=="GET":
			return JsonResponse(get_messages(request))
