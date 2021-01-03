from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
   

    return render(request, 'generator/home.html')



def password(request):
    lettersLower = string.ascii_lowercase
    lettersUpper = string.ascii_uppercase

    numb = string.digits
    punct = string.punctuation
    all = lettersLower
    if request.GET.get('upper'):
        all = all + lettersUpper
    
    if request.GET.get('numb'):

        all = all + numb

    if request.GET.get('character'):

        all = all + punct


    


    


    length = int(request.GET.get('length',13))
    allpasswd= ''.join(random.sample(all,length))

    return render(request, 'generator/password.html', { "passwd" : allpasswd }, )
    


