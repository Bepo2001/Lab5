from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.
people = []

class personalInfo(forms.Form):
    username=forms.CharField(label="username")
    password=forms.CharField(label="password")

class person:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def __str__(self):
        return self.username
    
def Default_path(request):
    return render(request, 'pageStyle\homePage.html',{'people':people})



def add(request): 
    if request.method == "POST":
        form1=personalInfo(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data["username"]
            password = form1.cleaned_data["password"]
            Person=person(username,password)
            people.append(Person)
            return HttpResponseRedirect('/home')
    else:
        form = personalInfo()
        return render(request, 'pageStyle/add.html', {'form': form, 'people': people})
            



