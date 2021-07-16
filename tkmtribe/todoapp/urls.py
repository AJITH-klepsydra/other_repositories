"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.rhome,name='rhome' ),
    path('home/',views.home,name="home" ),
    path('CodingCrew/',views.cc,name="cc" ),
    path('login/',views.LoginPage,name='login' ),
    path('profile/',views.Profile,name='profile' ),
    path('logout/',views.LogoutPage,name='logout' ),
    path('signup/',views.SignupPage,name='signup' ),
    path('submit/',views.submit_form,name="subm"),
    path('<int:val>/vote/',views.vote,name="vote"),
    path('<int:val>/flag/',views.flag,name="flag"),
    path('change/',views.change,name="change_claps"),
    path('<int:val>/comment/',views.comments,name="comments"),
    path('<int:val>/submit_comment/',views.comment_submission,name="comment_subm"),
    path('memesupload/',views.Upload,name='upload' ),
    path('memes/',views.memeshome,name='memes' ),
    path('inbox/',views.Inbox,name='inbox' ),
    path('<int:val>/meme_comment',views.memeComment,name='memecomment' ),
    path('<int:val>/meme_clap',views.memeClap,name='memeclap' ),
    path('<int:val>/meme_flag',views.memeFlag,name='memeflag' ),
    path('popular_memes/',views.PopularMemes,name='popular_memes' ),
    path('chatHome/',views.TkmChat,name='tkmchat' ),
    path('chatHome/<str:receiver>/',views.Chat,name='chat' ),
    path('post/ajax/submit',views.SendChat,name="send_chat"),
    path('post/ajax/notify',views.Notif,name="notify_tab"),
    path('post/ajax/tag_check',views.TagCheck,name="tag_check"),
    path('post/ajax/inbox_update',views.InboxUpdate,name="inbox_update"),
    path('post/ajax/home_data',views.home_data,name="home_data"),
]
