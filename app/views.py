from django.shortcuts import render
from app.models import *
# Create your views here.

def first(request):
    s=Student.objects.all()
    d={'stu':s}
    return render(request,'first.html',d)

def second(request):
    #Course.objects.filter(sname='Abishek').update(email='abishek@gmail.com')
    #Course.objects.filter(sname='Gopal').update(email='gopal123@gmail.com')
    #Course.objects.update_or_create(sname='Gokul',defaults={'cname':'Python'})
    #Course.objects.update_or_create(sname='Loganathan',defaults={'cname':'Sql','email':'loganathan@gmail.com'})
    #Course.objects.update_or_create(cname='Html',defaults={'email':'raja@gmail.com'})
    #w=Student.objects.get_or_create(sname='raja')[0]
    #w.save()
    #Course.objects.update_or_create(cname='Html',defaults={'sname':w,'email':'raja@gmail.com'})
    #Course.objects.filter(sname='raja').delete()
    #Course.objects.filter(sname='Gopal').delete()
    Course.objects.all().delete()
    c=Course.objects.all()
    d={'cou':c}
    return render(request,'second.html',d)

def third(request):
    i=Institite.objects.all()
    d={'ins':i}
    return render(request,'third.html',d)