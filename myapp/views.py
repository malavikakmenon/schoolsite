from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader #for template
# Create your views here.
from django.db import connection

from datetime import datetime

from django.contrib import messages

import uuid

# from django.core.mail import EmailMessage
from django.core.mail import send_mail
# from .forms import addstudentform
from django.shortcuts import render
from .forms import addstudentForm





# from django.conf import settings

# from django.core.mail import send_mail

# Create your views here.
def rfact(c,r):
    return {i[0]:r[c.description.index(i)] for i in c.description}

def table(request):
    stat=''
    c=connection.cursor()
    c.cursor.row_factory=rfact
    c.execute("select * from card")
    r=c.fetchall()
    dl=[]
    if r:
        dl=r
    print(dl)
    return render(request,'table.html',{'msg':stat,'card':dl})
    
def subject(request):
    stat="" 
    dl=[]
    c=connection.cursor()
    c.cursor.row_factory=rfact
    c.execute("select * from card")
    r=c.fetchall()
    dl=[]
    if r:
        dl=r
    print(dl)
     # return render(request,'subject.html',{'msg':stat,'card':dl})
    print(request.method)
    if request.method=='POST':
      print(request.method)
      snam=request.POST["subname"]
      mscore=request.POST["score"]
      sql=f"INSERT INTO card(subjects,maxscore)VALUES('{snam}','{mscore}')"
      c=connection.cursor()
      c.execute(sql)
      n=c.lastrowid
      c.close()
      if n>=0:
            return HttpResponseRedirect('/table/',request) 


      return HttpResponseRedirect('/subject/',request)  
       
    return render(request,'subject.html',{'msg':stat,'card':dl})

def delsub(request,subid):
    c=connection.cursor()
    c.execute(f"DELETE FROM card WHERE id={subid}")
    c.close()
    print('removed',subid)
    return HttpResponseRedirect('/subject/',request)

def editsub(request,subjid):
    stat=''
    dl=[]
    print(request.method)
    if request.method=='POST':
      print(request.method)
      sn=request.POST["editsub"]
      ns=request.POST["subnew"]
    c=connection.cursor()
    c.execute(f"UPDATE card SET subjects='{ns}' WHERE id='{subjid}'")
    c.close()
    print(' successfully updated',subjid)
    return HttpResponseRedirect('/subject/',request)

def facultylogin(request):
    stat="" 
    dl=[]
    print(request.method)
    if request.method=='POST':
      print(request.method)
      nam=request.POST["name"]
      mail=request.POST["emailid"]
      # pswd=request.POST["pswd"]
      ph=request.POST["mob"]
      print ("The random id : ",end="") 
      string=uuid.uuid4().hex
      newstr=string[-4:]
      print(newstr)

      dateTimeObj = datetime.now()
      sqlb=f"INSERT INTO userdetails(name,email,password,phoneno,datetime)VALUES('{nam}','{mail}','{newstr}','{ph}','{dateTimeObj}')"
      c=connection.cursor()
      c.execute(sqlb)
      # n=c.lastrowid
      c.close()
      
      # email = EmailMessage('test mail', f"successfully created account with password:'{newstr}'",to=[mail])
      # email.send()
    
      messages.success(request, f" Your password has been sent to registered email:'{mail}'")

      send_mail( f"Hello'{nam}' Your registration was successful",f"successfully created new account with password:'{newstr}'",'djangopy2020@gmail.com',[mail], fail_silently=False,)
     



      return HttpResponseRedirect('/facultylogin/',request)  

       
    return render(request,'facultylogin.html',{'msg':stat,'card':dl})

def login(request):
  print(request)
  stat=""
  if request.method=='POST':
    unam=request.POST["emailid"]
    pwd=request.POST["pswd"]
    c=connection.cursor()
    c.execute(f"select * from userdetails where email='{unam}'and password='{pwd}'")
    r=c.fetchone()
    c.close()
    if r: #unam=="admin" and pwd=="admin.123":
      request.session['usr']=unam
      return HttpResponseRedirect('/table/',request)
    stat="Invalid login..try again"
  t=loader.get_template('login.html')
  return HttpResponse(t.render({'msg':stat},request))



def signup(request):
    form= addstudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/studentlogin/')
  
    context= {'form': form }
        
    return render(request, 'signup.html', context)

def thankform(request):
    return HttpResponse("Welcome to your account")

def studlogin(request):
  print(request)
  stat=""
  if request.method=='POST':
    un=request.POST["username"]
    ps=request.POST["password"]
    c=connection.cursor()
    c.execute(f"select * from myapp_addstudent where email='{un}'and password='{ps}'")
    r=c.fetchone()
    c.close()
    if r: #unam=="admin" and pwd=="admin.123":
      request.session['usr']=un
      return HttpResponseRedirect('/thanks/',request)
    stat="Invalid login..try again"
  t=loader.get_template('studlogin.html')
  return HttpResponse(t.render({'msg':stat},request))

def payment(request):
  return render(request,'payment.html')
def index(request):
    return render(request,'index.html')

