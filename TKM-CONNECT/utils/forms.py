from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q
User=get_user_model()
class UserCreationForm(forms.ModelForm):
	password1=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'pass','placeholder':'Password'}))
	password2= forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'pass','placeholder':"Confirm Password"}))
	username=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'pass','placeholder':"Username"}))
	email=forms.CharField(label="",widget=forms.EmailInput(attrs={'class':'pass','placeholder':"email address"}))
	class Meta:
		model=User
		fields=['is_alumni','username','email',]
	def clean_password(self):
		password1=self.cleaned_data.get('password1')
		password1=self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match")
		return password2
	def save(self,commit=True):
		user=super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class UserLoginForm(forms.Form):
	query = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'someclass','placeholder':'Username/EmailId'}))
	password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'pass','placeholder':'Password'}))


	def clean(self,*args,**kwargs):
		query = self.cleaned_data.get('query')
		password=self.cleaned_data.get('password')
		query_qs_final = User.objects.filter(
				Q(username__iexact=query) |
				Q(email__iexact=query)
			).distinct()
		if not query_qs_final.exists() and query_qs_final.count != 1:
			raise forms.ValidationError("Invalid Credentials")
		user_obj=query_qs_final.first()
		if not user_obj.check_password(password):
			raise forms.ValidationError("Invalid Credentials")
		self.cleaned_data['user_obj']=user_obj
		return super(UserLoginForm, self).clean(*args,**kwargs)