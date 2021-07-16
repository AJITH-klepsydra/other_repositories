from django import forms
from .models import *
class job_post_form(forms.ModelForm):
	title=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'Job Title'}))
	interests=forms.ModelMultipleChoiceField(label="",widget=forms.CheckboxSelectMultiple,queryset=Interest.objects.all())
	description=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'desc','placeholder':'Description'}))
	#expiry=forms.CharField(label="",widget=forms.DateTimeInput(attrs={'class':'pass','placeholder':'Date of expiry'}))
	image=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'link to an image'}))

	class Meta:
		model=Job_post
		fields=['title','interests','description','image']
class ProjectForm(forms.ModelForm):
	title=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'Project Title'}))
	description=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'desc','placeholder':'Description'}))
	link=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'link to your project'}))
	class Meta:
		model=Project
		fields=['title','description','link']
class ProfileForm(forms.ModelForm):
	Dob=forms.CharField(label="",widget=forms.DateInput(attrs={'class':'pass','placeholder':'Date of birth'}))
	insta_id=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'Instagram ID '}))
	linkedin=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'Linkedin Id '}))
	image=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':' Link to your image '}))
	nick_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':' Nick name '}))
	class Meta:
		model=Profile
		fields=['department','semester','Dob','insta_id','linkedin','nick_name','image']
class BlogForm(forms.ModelForm):
	title=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'Title '}))
	description=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'desc','placeholder':'Description'}))
	link=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':'provide a link to know more'}))
	class Meta:
		model=Blog
		fields=['title','description','link']



