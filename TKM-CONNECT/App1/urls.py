from django.urls import path
from .views import *
urlpatterns=[
	path('',Home,name="home"),
	path('login/',Login,name="login"),
	path('logout/',Logout ,name="logout"),
	path('signup/',Signup,name="signup"),
	path('submit/',Job_Submits,name="submit"),
	path('add_projects/',AddProject,name="add-projects"),
	path('add_blog/',AddBlog,name="add-blogs"),
	path('edit_profile/',Editprofile,name="profedit"),
	path('profile/<int:val>/',Profile,name="profile"),
	path('chat/',Chat,name="chat"),
	path('ajax/post/',Savemsg,name="sendmsg"),
	path('ajax/fetch/',Showmsg,name="recmsg"),
]