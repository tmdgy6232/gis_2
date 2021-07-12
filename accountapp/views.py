from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def helloworld(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        helloWorldInstance = HelloWorld()
        helloWorldInstance.text = temp
        helloWorldInstance.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list})
