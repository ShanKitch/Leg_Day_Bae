from django.shortcuts import render,  redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import bcrypt 
import re
from .forms import ProfileForm , PartialProfileForm, ForumMessageForm










exerciselist={
    "1": "Running",
    "2": "Weight Training",
    "3": "HIIT",
    "4": "Yoga",
    "5": "Pilates",
    "6": "Crossfit",
    "7": "Dance Fitness",
    "8": "Cycling",
    "9": "Aerobics",
    "10": "Swimming"
}

def index(request):
    return render (request, 'login.html')

def register(request):
    if request.method=='POST':
        errors=User.objects.reg_validator(request.POST)
        if len(errors) !=0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        hashed_pw=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], 
        username=request.POST['username'], password=hashed_pw)
        request.session['user']=new_user.first_name
        request.session['user_id']=new_user.id
        request.session['username']=new_user.username
        return redirect('/create')
    return redirect('/create')

def login(request):
    if request.method=='POST':
        errors=User.objects.log_validator(request.POST)
        if len(errors) !=0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        this_user=User.objects.get(email=request.POST['email'])
        request.session['user_id']= this_user.id
        print(request.session['user_id'])
        request.session['user']=this_user.first_name
        request.session['username']=this_user.username

        
        

        return redirect('/home')
    return redirect('/home')


def home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context={
       'profiles' : Profile.objects.all()

  
    }    
    return render(request, 'home.html', context)



def create(request):
    if 'user_id' not in request.session:
        return redirect('/')
    form = ProfileForm(request.POST) 
    context={
        'profileform':form,
    }
    return render(request, 'create.html', context)

def create_profile(request):
    if request.method == 'POST':
        errors=Profile.objects.profile_validator(request.POST)
        if len(errors) !=0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/create')
        form = ProfileForm(request.POST, request.FILES) 
        owner_id=request.session['user_id']
        workout_type =request.POST.getlist('workout_type')
        Profile.objects.create(
            owner=User.objects.get(id=owner_id),
            workout_type=",".join(workout_type),
            new_exercise=request.POST['new_exercise'],
            frequency=request.POST['frequency'],
            time_day=request.POST['time_day'],
            age=request.POST['age'],
            sex=request.POST['sex'],
            location_city=request.POST['location_city'],
            location_state=request.POST['location_state'],
            img=request.FILES['img']
        )
    print(request.POST.getlist('workout_type'))
    print(request.POST['sex'])
    print(request.FILES)
    return redirect('/home')

def view_user(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    owner=User.objects.get(id=id)
    context={
        'profiles': Profile.objects.filter(owner=User.objects.get(id=id)), 
        'username': User.objects.get(id=id).username
    }
    print(owner)
    print(request.session['user_id'])
    return render (request,'view.html',context)



def update(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    owner=User.objects.get(id=id)
    this_profile=Profile.objects.get(owner=User.objects.get(id=id))
    workout_type =request.POST.getlist('workout_type')
    initial_dict={
        'owner': owner,
        'new_exercise': this_profile.new_exercise,
        'frequency': this_profile.frequency,
        'time_day': this_profile.time_day,
        'age': this_profile.age,
        'sex': this_profile.sex,
        'location_city':this_profile.location_city,
        'location_state': this_profile.location_state,
        'img': this_profile.img,

    }
    form = PartialProfileForm(initial=initial_dict, instance=this_profile)
        
    context={
        'username': User.objects.get(id=id).username,
        'this_profile': this_profile,
        'update_form' : form
      
    }
    print (this_profile)
    print(this_profile.age)
    print (request.session['user_id'])
    return render(request, 'update.html', context)

def update_profile(request):
    if 'user_id' not in request.session:
        return redirect('/')
        
    if request.method=='POST':
        owner=request.session['user_id']
        this_profile=Profile.objects.get(owner=owner)
        update_form= PartialProfileForm(request.POST, request.FILES, instance=this_profile)
        if update_form.is_valid():
           profile=update_form.save()
        


        
    # this_profile.age=request.POST['age']
    # this_profile.new_exercise=request.POST['new_exercise']
    this_profile.save()
    print(this_profile.age)
    return redirect('/home')


def inbox(request):
    if 'user_id' not in request.session:
        return redirect('/home')
    this_user = User.objects.filter(id=request.session['user_id'])
    if len(this_user) != 1:
        return redirect('/home')
    elif this_user[0].id != request.session['user_id']:
        return redirect('/home')
    context = {
        'user': this_user[0],
        'messages': this_user[0].sent_to.all(), 
        'sent_messages': this_user[0].sent_from.all(),
       
       
    }
    return render(request, 'inbox.html', context)


def send_message(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method=="POST":
        recipient=User.objects.filter(username=request.POST['recipient'])
        print(recipient)
        new_message = Message.objects.create(
            message=request.POST['message'], 
            subject=request.POST['subject'], 
            sender=User.objects.get(id=request.session['user_id']), 
            recipient=User.objects.get(id=recipient[0].id)
        )

  
    return redirect('/home')

def reply_message(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method=="POST":
        print(request.POST)
        new_message = Message.objects.create(
            message=request.POST['message'], 
            subject=request.POST['subject'], 
            sender=User.objects.get(id=request.session['user_id']), 
            recipient=User.objects.get(id=request.POST['recipient'])
        )
# <QueryDict: {'csrfmiddlewaretoken': ['Ni0YOZgS8cYZpEdR3dGmD54jzn2Yg3qNmKVqNfuEVR48DzKMimeWeFL97RQcgEtN'],
#  'sender': ['FriendlySpiderman'], 'subject': ['Re: Running'], 'message': ['Test'], 'recipient': ['25']}>    

    return redirect('/inbox')

def delete_message(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')

    deleted_message=Message.objects.get(id=message_id)
    deleted_message.delete()
    return redirect('/inbox')

def mark_as_read(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')

    this_message = Message.objects.get(id=message_id)
    this_message.read = True
    this_message.save()
    return redirect('/inbox')


def mark_as_unread(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_message = Message.objects.get(id=message_id)
    this_message.read = False
    this_message.save()
    return redirect('/inbox')


def forum (request):
    if 'user_id' not in request.session:
        return redirect ('/')  
    context= {
        'forum_posts': Forum_Message.objects.all(),

       

    } 
    return render (request, 'forum.html', context)

def forum_post (request):
    if 'user_id' not in request.session:
        return redirect('/')
    Forum_Message.objects.create(
        message_subject=request.POST['message_subject'],
        forum_message=request.POST['forum_message'], 
        poster=User.objects.get(id=request.session['user_id'])
        )
    return redirect('/forum')



def post_comment(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_message=Forum_Message.objects.get(id=id)
    Forum_Comment.objects.create(
        comment=request.POST['post_comment'], 
        poster=User.objects.get(id=request.session['user_id']), 
        forum_message=this_message)
    return redirect('/forum')


def delete_comment(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    destroyed = Forum_Comment.objects.get(id=id)
    destroyed.delete()
    return redirect('/forum')

def delete_post(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    destroyed_post = Forum_Message.objects.get(id=id)
    destroyed_post.delete()
    return redirect('/forum')

def reply_comment(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_comment=Forum_Comment.objects.get(id=id)
    Comment_Reply.objects.create(
        reply_comment=request.POST['reply_comment'],
        poster=User.objects.get(id=request.session['user_id']),
        forum_comment=this_comment
    )
    return redirect('/forum')

def delete_reply(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    destroy_reply=Comment_Reply.objects.get(id=id)
    destroy_reply.delete()
    return redirect('/forum')
