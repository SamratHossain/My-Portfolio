from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html',{'title':'Home'})

def project(request):
    return render(request, 'home/project.html',{'title':'Project'})

def skill(request):
    return render(request, 'home/skill.html',{'title':'Skill'})

def contact(request):
    return render(request, 'home/contact.html',{'title':'Contact'})
