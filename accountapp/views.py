from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    print(request.get_port())
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text':'postmethod'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text':'getmethod'})