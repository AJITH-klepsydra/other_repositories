from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CreateForm
from .models import confess,comment,CreateForm,Memes,Feedback,UserPair,User,Chats
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
#from django.core.mail import send_mass_mail
from django.conf import settings
from django.http import JsonResponse
import time
import datetime
from django.views.decorators.csrf import csrf_exempt
import requests

'''
    User authentication
'''
#Login page rendering and redirect to home page after authentication
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('rhome')
    else:
        if request.method == 'POST':
            username = request.POST['user_name']
            password = request.POST['user_password']
            user = authenticate(request,username=username,password=password)
            if(user is not None):
                login(request,user)
                return redirect('rhome')
        else:
            messages.info(request,"Incorrect")
        return render(request,'login.html',{})
#add new object to the user model
def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateForm()
        if(request.method=='POST'):
            form = CreateForm(request.POST)
            if(form.is_valid()):
                form.save()
                user = form.cleaned_data.get('username')
                #messages.success(str(request.user)+' Added to the database')
                return redirect('login')
        context={'form':form}
        return render(request,'signup.html',context)

'''
    Bright Side
'''
#Bright Side home page returning confess objects
@login_required(login_url='login')
def home(request):
    arranged_mgs =confess.objects.all().order_by('-pub_date')

    return render(request,'index.html',{'arranged_mgs':arranged_mgs,'users':User.objects.all()})
#confession Submission
@login_required(login_url='login')
def submit_form(request):
    msg = request.POST['search']
    usr= request.POST['user']
    if(msg):
        confess.objects.create(subm_text=msg,user=usr,post_muthalali=request.user,tagged_users=request.POST['tag1'])
        for user in User.objects.all():
            user.inbox_set.create(message=str(request.user)+" Posted something on the Bright side <a href='https://the-tkm-tribe.herokuapp.com/home/'> click here </a> ", type="bright_side"  )

        tag_list=request.POST['tag1'].split(',')
        print(tag_list)
        for tag in tag_list:
            print(tag)
            try:
                chat_id = (User.objects.all().get(username=tag)).telegram_chat_id
                url = "https://api.telegram.org/bot1140388120:AAENopa2fHGH_KpvcxwiQ2KrKJcuxaOA8rg/sendMessage?text={}&chat_id={}".format(str(usr)+' tagged u in a post '+' https://the-tkm-tribe.herokuapp.com/inbox/',chat_id)
                requests.get(url)
            except:
                pass
        arranged_mgs =confess.objects.all().order_by('-pub_date')
        return redirect(request.META['HTTP_REFERER'],'index.html',{'arranged_mgs':arranged_mgs})
    else:
        return redirect(request.META['HTTP_REFERER'])
#vote for each confession
@login_required(login_url='login')
def vote(request,val):
    q=confess.objects.get(pk=val)
    print(request.user)
    flag = 1
    for user in q.userchoice_set.all():
        if(str(user.user_name) == str(request.user)):
            flag = 0
    if(flag == 1):
        pub_date = q.pub_date
        q.claps+=1
        q.save()
        q.userchoice_set.create(user_name=request.user)
    arranged_mgs =confess.objects.all().order_by('-pub_date')
    return redirect(request.META['HTTP_REFERER'],'index.html',{'arranged_mgs':arranged_mgs})
#flag for each confess
@login_required(login_url='login')
def flag(request,val):
    q=confess.objects.get(pk=val)
    print(request.user)
    flag = 1
    for user in q.userflags_set.all():
        if(str(user.user_name) == str(request.user)):
            flag = 0
    if(flag == 1):
        q.flags+=1
        q.save()
        q.userflags_set.create(user_name=request.user)
    arranged_mgs =confess.objects.all().order_by('-pub_date')
    return redirect(request.META['HTTP_REFERER'],'index.html',{'arranged_mgs':arranged_mgs})
#comment page
@login_required(login_url='login')
def comments(request,val):
    arranged_mgs =confess.objects.all().order_by('-pub_date')
    post_msg_obj = confess.objects.all().get(pk = val)
    post_msg=post_msg_obj.subm_text
    #comments = post_msg_obj.comment
    post_id=val
    comment_list= post_msg_obj.comment_set.all().order_by('-comment_pub_date')

    return render(request,'comments.html',{'post_msg':post_msg,'post_id':post_id,'comment_list':comment_list,'mg':post_msg_obj})
'''
    Coding crew page
'''
#Coding crew page future implementation
@login_required(login_url='login')
def cc(request):
    arranged_mgs =confess.objects.all().order_by('-pub_date')
    return render(request,'admin.html',{'arranged_mgs':arranged_mgs})
'''
    Admin page updation
'''
#change vote per 10
@login_required(login_url='login')
def change(request):
    id=request.POST['change_it']
    q = confess.objects.all().get(pk=id)
    q.claps+=10
    q.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def comment_submission(request,val):
    comment_post = request.POST['comment']
    if(comment_post):
        conf_obj = confess.objects.all().get(pk=val)
        conf_obj.comment_set.create(comment=comment_post)
    return redirect(request.META['HTTP_REFERER'])
def LogoutPage(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def Upload(request):
    if(request.method=='POST'):
        uplaoded_file = request.FILES['document']
        meme_author = request.POST['auth_name']
        meme_caption=request.POST['meme_caption']
        meme_hub=request.POST['hub_name']

        Memes.objects.create(meme_author = meme_author,meme_caption=meme_caption,meme_hub=meme_hub,meme_image=uplaoded_file)

        memes_dic=Memes.objects.all()
        return redirect('memes')


    return render(request,'upload.html',{})
@login_required(login_url='login')
def memeshome(request):
    memes_dic=Memes.objects.all().order_by('-pub_date')

    return render(request,'memes.html',{'memes_dic':memes_dic,'media_url':settings.MEDIA_URL})
@login_required(login_url='login')
def rhome(request):
    if(request.method=="POST"):
        Feedback.objects.create(name=request.POST['name'],email=request.POST['email'],message=request.POST['message'])
        return render(request,'rhome.html',{})
    return render(request,'rhome.html',{})

@login_required(login_url='login')
@csrf_exempt
def home_data(request):
    print("HII")
    if(request.is_ajax and request.method == 'POST'):
        ls ={}
        i=0
        for con in confess.objects.all().order_by('-pub_date'):
            print(con.id)
            u =User.objects.all().get(username = con.post_muthalali)
            ls[i] = {"content":con.subm_text,"pub_date":con.pub_date,"user_name":u.username,"image":u.profile_icon,'id':con.id,'likes':con.claps,'flags':con.flags,}
            i +=1
        return JsonResponse(ls,status=200)


@login_required(login_url='login')
def memeComment(request,val):
    o=Memes.objects.all().get(pk=val)
    if(request.method=='POST'):
        o.memecomments_set.create(comment_author=request.user,comment_text=request.POST['comment'],)
        meme_comments = o.memecomments_set.all().order_by('-comment_pub_date')
        return render(request,'memecomments.html',{'o':o,'media_url':settings.MEDIA_URL,'meme_comments':meme_comments})
    meme_comments = o.memecomments_set.all().order_by('-comment_pub_date')
    return render(request,'memecomments.html',{'o':o,'media_url':settings.MEDIA_URL,'meme_comments':meme_comments})
@login_required(login_url='login')
def memeClap(request,val):
    q=Memes.objects.get(pk=val)

    flag = 1

    for user in q.memeclaps_set.all():
        #print(user.user_name)
        #print(request.user)
        if(str(user.user_name) == str(request.user)):
            #print('true')
            flag = 0

    if(flag == 1):
        q.claps+=1
        q.save()
        q.memeclaps_set.create(user_name=request.user)

    memes_dic=Memes.objects.all().order_by('-pub_date')
    return render(request,'memes.html',{'memes_dic':memes_dic,'media_url':settings.MEDIA_URL})
@login_required(login_url='login')
def memeFlag(request,val):
    q=Memes.objects.get(pk=val)
    flag = 1

    for user in q.memeflags_set.all():
        #print(user.user_name)
        #print(request.user)
        if(str(user.user_name) == str(request.user)):
            #print('true')
            flag = 0

    if(flag == 1):
        q.flags+=1
        q.save()
        q.memeflags_set.create(user_name=request.user)

    memes_dic=Memes.objects.all().order_by('-pub_date')
    return render(request,'memes.html',{'memes_dic':memes_dic,'media_url':settings.MEDIA_URL})
@login_required(login_url='login')
def PopularMemes(request):
        memes_dic=Memes.objects.all().order_by('-claps')
        return render(request,'memes.html',{'memes_dic':memes_dic,'media_url':settings.MEDIA_URL})
'''
    TkmChat
'''


#for loding user screen
@login_required(login_url='login')
def TkmChat(request):

    for u in User.objects.all():
        print(u.username,u.last_scene,datetime.datetime.now())
        if(datetime.datetime.now() < u.last_scene+datetime.timedelta(seconds=100) ):
            u.online='True'
            u.save()
        else:
            u.online='False'
            u.save()
    context={'users':User.objects.all(),'current_user':str(request.user),'current_date':datetime.datetime.now(),}
    if(request.method=='POST'):
        search = request.POST['user_name_search']
        context={'users':User.objects.all().filter(username__contains=search),'current_user':str(request.user),'current_date':datetime.datetime.now(),}
        return render(request,'chathome.html',context)
    return render(request,'chathome.html',context)
@login_required(login_url='login')
def Chat(request,receiver):
    try:

        UserPair.objects.create(user_pair = str(receiver))
    except:
        pass
    return render(request,'room.html',{'receiver':receiver,'current_user':str(request.user)})

def jasonise(userpair):
    u = UserPair.objects.all().get(user_pair=userpair)
    i=0
    ls = {}
    for obj in u.chats_set.all().order_by('-timestamp'):
        ls[i]={'sender':obj.sender,'receiver':obj.receiver,'content':obj.content,'pub_date':str(obj.timestamp)}
        i=i+1
    return ls



@login_required(login_url='login')
def SendChat(request):
    if(request.is_ajax and request.method=='POST' and request.POST['chat_text']):
        u = UserPair.objects.all().get(user_pair=request.POST['userpair'])
        if(request.POST['userpair']=='global'):
            u.chats_set.create(sender=str(request.user),receiver='global',content=request.POST['chat_text'])
            for user in User.objects.all():
                user.inbox_set.create(message=str(request.user)+" Sended a message in TKMChat Global <a href='https://the-tkm-tribe.herokuapp.com/chatHome/global/'> click here </a> ", type="global"  )

        else:
            receiver = request.POST['userpair'].replace('_chat_with_','')
            receiver=receiver.replace(str(request.user),'')
            chat=u.chats_set.create(sender=str(request.user),receiver=receiver,content=request.POST['chat_text'])
            user = User.objects.all().get(username=receiver)
            user.inbox_set.create(message=str(request.user)+" just send you a message <a href='https://the-tkm-tribe.herokuapp.com/chatHome/"+request.POST['userpair']+ "/'> click here </a> ", type="personal"  )

            chat_id = User.objects.all().get(username=receiver).telegram_chat_id
            url = "https://api.telegram.org/bot1140388120:AAENopa2fHGH_KpvcxwiQ2KrKJcuxaOA8rg/sendMessage?text={}&chat_id={}".format('New message '+'https://the-tkm-tribe.herokuapp.com/inbox/',chat_id)
            print(url)
            requests.get(url)

        context={
            'chats':jasonise(request.POST['userpair']),
        }
        return JsonResponse(context, status=200)
    elif(request.is_ajax and request.method=='GET'):
        context={
            'chats':jasonise(request.GET['userpair']),
                }

        return JsonResponse(context, status=200)
@csrf_exempt
def TagCheck(request):
    ls={}
    i=0
    if(request.is_ajax and request.method=='POST'):
        if(request.POST['tag1']):
            for user in User.objects.all().filter(username__contains=request.POST['tag1']):
                ls[i]=user.username
                i=i+1
                return JsonResponse(ls, status=200)
        else:
            ls[0]=''
            return JsonResponse(ls, status=200)
@csrf_exempt
def OnlineCheck(request):
    if request.is_ajax and request.method=='POST':
        ls={'users':User.objects.all()}
        return JsonResponse(ls, status=200)
@login_required(login_url='login')
def Inbox(request):
    u=User.objects.all().get(username=request.user.username)
    inBox=u.inbox_set.all().order_by('-timestamp')
    i=0
    ls ={}
    for obj in inBox:
        ls[i]={'message':obj.message,'type':obj.type,'timestamp':str(obj.timestamp)}
        i = i+1
    context={'inbox':ls,}
    return render(request,'inbox.html',context)
def Notif(request):
    if(request.is_ajax() and request.method=='GET'):
        u=User.objects.all().get(username=request.user.username)
        inBox=u.inbox_set.all().order_by('-timestamp')[0]
        color='black'
        if(datetime.datetime.now()-inBox.timestamp<datetime.timedelta(minutes=30)):
            color='green';
        ls ={'message':inBox.message,'timestamp':inBox.timestamp,'type':inBox.type,'color':color}
        return JsonResponse(ls, status=200)
def InboxUpdate(request):
    if(request.is_ajax() and request.method=='POST'):
        u=User.objects.all().get(username=request.user.username)
        if(request.POST['hey']=='all'):
            inBox=u.inbox_set.all().order_by('-timestamp')
            i=0
            ls ={}
            for obj in inBox:
                ls[i]={'message':obj.message,'type':obj.type,'timestamp':str(obj.timestamp)}
                i = i+1
            context={'inbox':ls,}
            return JsonResponse(context, status=200)
        else:
            inBox=u.inbox_set.all().filter(type=request.POST['hey']).order_by('-timestamp')
            i=0
            ls ={}
            for obj in inBox:
                ls[i]={'message':obj.message,'type':obj.type,'timestamp':str(obj.timestamp)}
                i = i+1
            context={'inbox':ls,}
            return JsonResponse(context, status=200)
@login_required(login_url='login')
def Profile(request):
    u=User.objects.all().get(username=request.user.username)
    if(request.method=="POST"):
        u=User.objects.all().get(username=request.user.username)
        u.profile_icon = request.POST['profile_icon']
        u.username = request.POST['username']
        u.email = request.POST['email']
        u.telegram_chat_id = request.POST['telegram']
        u.save()
    return render(request,'profile.html',{'u':u,})
