from django.contrib import admin
from django.urls import path,re_path,include
from .views import IndexView,DetailView, CategoryView, TagView,AboutView

urlpatterns = [
    # re_path(r'^$', IndexView.as_view(), name='index'),  # 主页，自然排序
    # re_path(r'^hot/$',IndexView.as_view(),{'sort':'v'},name='index_hot'), #主页，按照热度排序
    # re_path(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),  # 文章内容页
    path('', IndexView.as_view(), name='index'),  # 主页，自然排序
    path('hot/', IndexView.as_view(), {'sort': 'v'}, name='index_hot'),  # 主页，按照浏览量排序
    path('article/<slug:slug>/', DetailView.as_view(), name='detail'),  # 文章内容页
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('category/<slug:slug>/hot/', CategoryView.as_view(), {'sort': 'v'},name='category_hot'),
    path('tag/<slug:slug>/', TagView.as_view(), name='tag'),
    path('tag/<slug:slug>/hot/', TagView.as_view(), {'sort': 'v'}, name='tag_hot'),
    path('about/', AboutView, name='about'),  # About页面
]