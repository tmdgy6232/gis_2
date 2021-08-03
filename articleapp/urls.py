from django.urls import path, include
from django.views.generic import TemplateView
from articleapp.views import ArticleCreateView, ArticleDetailView

app_name = 'articleapp'

#templateView = 로직없이 어떤 html을 쓸건지 말해주면 템플릿만 보여주는 기능을 함

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'),name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
]

