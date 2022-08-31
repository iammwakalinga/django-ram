from base64 import urlsafe_b64encode
from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from my_kingdom import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from . tokens import generate_token
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode






def index(request):

    return render(request,'index.html')




def signup(request):

    if request.method == "POST":
       # username = request.POST.get('username')
       username = request.POST['username']
       fname = request.POST['fname']
       lname = request.POST['lname']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']

       if User.objects.filter(username=username):
           messages.error(request,"Username already exist!Please try some other username")
           return redirect('index')
       if User.objects.filter(email=email):
               messages.error(request,"Email already exist!Please try some other username")
               return redirect('index')
       if len(username)>10:
               messages.error(request,"Username must be under 10 character")
               return redirect('index') 
       if  not username.isalnum():
               messages.error(request,"Password didn't match!")
               return redirect('index') 
       if pass1 != pass2:
               messages.error(request,"Username must be Alpha-numeric!")
               return redirect('index') 
           
          

       myuser = User.objects.create_user(username,email,pass1)
       myuser.first_name = fname
       myuser.last_name = lname
       myuser.is_active = False

       myuser.save( )


       messages.success(request, "Your Account has been successfully created.We have sent you a confirmation email,please confirm your email in order to activate your account")

       subject = "Welcome to Django-Login"
       message = "Hello"+ myuser.first_name + "!!\n" + "Welcome to Django!!\n Thank you for visiting our  website\n We have also sent you a confirmation email,please confirm your email address in order to activate your account. \n\n Thanking You \n Raidin Mwakalinga"
       from_email = settings.EMAILS_HOST_USER
       to_list = [myuser.email]
       send_mail(subject,message,from_email,to_list,fail_silently=True)

       current_site =  get_current_site(request)
       email_subject = "Confirm your email Django"
       message2 = render_to_string('email_confirmation.html',{
       
         'name':myuser.first_name,
         'domain':current_site.domain,
         'uid':urlsafe_base64_encode (force_bytes(myuser.pk)),
         'token':generate_token.make_token(myuser)

       })
       email = EmailMessage(
           email_subject,
           message2,
           settings.EMAIL_HOST_USER,
           [myuser.email],
       )
       email.fail_silently = True
       email.send()



       return redirect('signin')

    return render(request,"signup.html")


def signin(request): 
    if request.method == "POST":  
      username = request.POST['username']
      pass1 = request.POST['pass1']
      user = authenticate (username=username,password=pass1)

      if user is not None:
          login(request,user)
          fname = user.first_name
          return render(request,"index.html",{'fname':fname})
    

         
      else:
        messages.error(request,"Bad Credentials!")
        return redirect('index')

    return render(request,"signin.html")   

def signout(request):
    logout(request)
    messages.success(request,"loggeed out Successfully")
    return redirect('index')


def activate(request,uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_activate = True
        myuser.save( )
        login(request,myuser)
        return redirect('index')
    else:
        return render(request,'activation_failed.html')









































