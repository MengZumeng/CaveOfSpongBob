from django.contrib import admin

# Register your models here.
from .models import Keyword,Tag,Category,Article,Timeline,Carousel,Silian

admin.site.register(Keyword)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Timeline)
admin.site.register(Carousel)
admin.site.register(Silian)
