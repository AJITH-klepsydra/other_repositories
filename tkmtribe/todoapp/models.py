from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime
'''
    UserCreation form
'''
class User(User):
    telegram_chat_id = models.IntegerField(default=0)
    last_scene = models.DateTimeField(auto_now=False,default=datetime.datetime(2018, 6, 15, 14, 0, 47, 552447,))
    online = models.CharField(default='False',max_length=5)
    profile_icon=models.CharField(max_length=300)
class CreateForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2','email','telegram_chat_id','profile_icon']

#MainPage Feedback session
class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.name

'''
    Bright side Page
'''
#confession store
class confess(models.Model):
    subm_text = models.CharField(max_length = 5000)
    user = models.CharField(max_length=100,default='anonymous')
    tagged_users = models.CharField(max_length=100,default='')
    claps = models.IntegerField(default=0)
    flags =models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add =True)
    post_muthalali = models.CharField(max_length=50,default='Unknown')
    def __str__(self):
        return str(self.pk)
#Clap for each message
class UserChoice(models.Model):
    conf_obj = models.ForeignKey(confess,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,default='anonymous')
#flag for each message
class UserFlags(models.Model):
    conf_obj = models.ForeignKey(confess,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,default='anonymous')
#comment set for each confess
class comment(models.Model):
    confess_obj = models.ForeignKey(confess,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    comment_pub_date=models.DateTimeField(auto_now =True)

'''
    Memepage database
'''
#meme database
class Memes(models.Model):
    meme_author = models.CharField(max_length=30,default ='anonymous')
    pub_date = models.DateTimeField(auto_now=True)
    claps=models.IntegerField(default=0)
    flags=models.IntegerField(default=0)
    meme_caption = models.CharField(max_length=100)
    meme_hub = models.CharField(max_length=50,default="TkmMemes")
    meme_image = models.FileField(upload_to = 'Memes/images' )
    def __str__(self):
        return self.meme_caption
#comment set for each meme
class memecomments(models.Model):
    meme= models.ForeignKey(Memes,on_delete=models.CASCADE)
    comment_author=models.CharField(max_length=50)
    comment_text = models.CharField(max_length=150)
    comment_pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.meme_text
#claps for each meme
class memeclaps(models.Model):
    meme= models.ForeignKey(Memes,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,default='anonymous')
#flags for each meme
class memeflags(models.Model):
    meme= models.ForeignKey(Memes,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100,default='anonymous')

'''
    Chat section database
'''
#user pair group(each user pair will be having different db objects)
class UserPair(models.Model):
    user_pair = models.CharField(max_length=50,unique = True)

    def __str__(self):
        return self.user_pair
#db to store individual user_pair set of chat messages
class Chats(models.Model):
    userpair=models.ForeignKey(UserPair,on_delete=models.CASCADE)
    sender=models.CharField(max_length=30,default="unknown")
    receiver=models.CharField(max_length=30,default="unknown")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
class Inbox(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    type=models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
