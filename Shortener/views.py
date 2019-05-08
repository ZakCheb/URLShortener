from django.shortcuts import render,redirect
from   URLShortener.settings import SHORT_URL_LENGHT,DOMAIN

from .models import *
from .forms import *

def HomePage(request):
    form =InputNewUrl(request.POST or None)

    if form.is_valid():

        ShortURLObject = form.save(commit=False)
        ShortURLObject.short=UrlGenerator()
        ShortURLObject.save()
        form=InputNewUrl()
        UrlStr="http://{}/go/{}".format(DOMAIN,ShortURLObject.short)

        return render(request,"index.html",{
            'msg':'More?',
            'UrlStr':UrlStr,
            'f':form,
        })

    return render(request,"index.html",{'msg':'Insert Url to Shrink.','f':form})



def RedirectPage(request,target):
    
    try:
        link=ShortURL.objects.get(short=target)
    
    except ShortURL.DoesNotExist:
        
        return render(request,"index.html",{'msg':'Short Link do not exists.'})
    
    return redirect(link.original)



import random
import string
from   URLShortener.settings import SHORT_URL_LENGHT

def UrlGenerator(length=SHORT_URL_LENGHT):
    All = string.ascii_letters+string.digits
    return ''.join(random.choice(All) for i in range(length))