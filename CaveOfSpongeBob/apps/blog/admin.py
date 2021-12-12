from django.contrib import admin

# Register your models here.
from .models import Keyword,Tag,Category,Article,Carousel,TestClass,AboutBlog

admin.site.register(Keyword)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Carousel)
admin.site.register(TestClass)
admin.site.register(AboutBlog)