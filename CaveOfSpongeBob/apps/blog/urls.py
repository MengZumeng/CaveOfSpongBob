from django.contrib import admin
from django.urls import path,re_path,include
from .views import IndexView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),  # 主页，自然排序
]