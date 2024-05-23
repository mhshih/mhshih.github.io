from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, template_name='BSindex.htm', context={})

def home(request):
    return render(request, template_name="input.html", context={})

def photo(request):
    return render(request, template_name="photo.html", context={})

from week9project.models import User

def output2(request):
    un = request.GET['UserName']
    mail = request.GET['UserMail']

    u = User(username=un, email=mail)
    u.save()

    return render(request=request, template_name="users_template.html", context={"users_list": User.objects.all()})
