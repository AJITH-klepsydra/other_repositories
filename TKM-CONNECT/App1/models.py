from django.db import models
from utils.models import Member as User
from django.forms import ModelForm
class Product(models.Model):
	product_name=models.CharField(max_length=100,unique=True)
	description=models.CharField(max_length=500)
	image= models.ImageField(upload_to='product_images',blank=True)
	producer = models.ForeignKey(User, on_delete=models.CASCADE)
	count= models.IntegerField(default=0)
	up_date=models.DateTimeField(auto_now_add=True)
	expiry_date=models.DateTimeField()
	def __str__(self):
		return self.product_name




class Project(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	link=models.CharField(max_length=200)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
class Blog(models.Model):
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	description=models.TextField()
	link=models.CharField(max_length=200)
	def __str__(self):
		return self.title
class Interest(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	def __str__(self):
		return self.title

DEP_CHOICES=(("Cmputer science","CS"),("marine","MR"),("Mechanical","MECH"),("Not filled",""))
SEM_CHOICES=(("first",1),("second",2),("third",3),("not filled",0))
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#interests=models.ManyToManyField(Interest)
	Projects=models.ManyToManyField(Project)
	department=models.CharField(max_length=100,choices=DEP_CHOICES,default="")
	semester=models.CharField(max_length=100,choices=SEM_CHOICES,default=0)
	Dob=models.CharField(max_length=100)
	insta_id=models.CharField(max_length=100)
	linkedin=models.CharField(max_length=100)
	nick_name=models.CharField(max_length=100)
	image=models.CharField(max_length=200)
class Job_post(models.Model):
	alumni=models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=100,unique=True)
	interests=models.ManyToManyField(Interest)
	description=models.TextField()
	update=models.DateTimeField(auto_now_add=True)
	#expiry=models.DateTimeField()
	image=models.CharField(max_length=500)
	def __str__(self):
		return self.title

class Request(models.Model):
	job=models.ForeignKey(Job_post, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
	alumni=models.ForeignKey(User, on_delete=models.CASCADE,related_name="alumni")
	update=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "{} to {}".format(self.user,self.alumni)



class Query(models.Model):
	interests=models.ManyToManyField(Interest)
	question=models.CharField(max_length=200)
	description=models.CharField(max_length=800)
	image=models.ImageField(upload_to="query")

class Message(models.Model):
	message=models.CharField(max_length=500)
	sender = models.ForeignKey(User, on_delete=models.CASCADE)
	group = models.CharField(max_length=100) 
	date_time = models.DateTimeField(auto_now_add=True)  

"""
Admin, alumni, student
alumni -> detailed description , picture, id card ,contact details
student-> pojects(2),name contact details ,interested field
student inu request cheyyumbo chat option, decide
alumni post job opportunity and blog
edge
students can post queries
Home -> job posts, profile button, query post, logout, search for alumni
Alumni Home:   Vanna request, logout, chat of interest
post jobs
Ajith kumar P MToday at 01:39
free tier premium tier"""



