from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from articleapp.models import Article


# @login_required #(login_url=reverse_lazy('accountapp:create')) 로그인 url 디폴트값이 아닐 시에 수정
# def helloworld(request):
#     if request.method == "POST":
#         temp = request.POST.get('hello_world_input')
#         helloWorldInstance = HelloWorld()
#         helloWorldInstance.text = temp
#         helloWorldInstance.save()
#
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#     else:
#         hello_world_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
#

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)

has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get') # 메서드에는 원래 decorator를 적용할 수 없지만 method_decorator가 가능하게 해줌
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(has_ownership, 'get') # 메서드에는 원래 decorator를 적용할 수 없지만 method_decorator가 가능하게 해줌
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'
