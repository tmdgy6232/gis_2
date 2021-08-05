from django.urls import path, include
from django.views.generic import TemplateView
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

#templateView = 로직없이 어떤 html을 쓸건지 말해주면 템플릿만 보여주는 기능을 함

urlpatterns = [
    path('list/', ArticleListView.as_view(),name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]

