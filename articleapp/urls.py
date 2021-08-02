from django.urls import path, include
from django.views.generic import TemplateView

#templateView = 로직없이 어떤 html을 쓸건지 말해주면 템플릿만 보여주는 기능을 함
urlpatterns = [
    path('list', TemplateView.as_view(template_name='articleapp/list.html'),name='list')
]

