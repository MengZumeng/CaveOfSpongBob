from django.contrib import admin
from django.urls import path,re_path,include
from .views import IndexView,DetailView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),  # 主页，自然排序
    re_path(r'^hot/$',IndexView.as_view(),{'sort':'v'},name='index_hot'), #主页，按照热度排序
    re_path(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),  # 文章内容页
]