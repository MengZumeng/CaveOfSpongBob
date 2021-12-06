from .models import Article, Tag, Category, Timeline, Silian,TestClass
from django.views import generic
from django.conf import settings
from django.shortcuts import render

# Create your views here.
class IndexView(generic.ListView):
    # model = TestClass
    # template_name = 'blog/test.html'
    # context_object_name = '测试'
    # paginate_by = settings.BASE_PAGE_BY
    # paginate_orphans = settings.BASE_ORPHANS


    # def get_ordering(self):
    #     ordering = super(IndexView, self).get_ordering()
    #     sort = self.kwargs.get('sort')
    #     if sort == 'v':
    #         return ('-views','-update_date','-id')
    #     return ordering
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = settings.BASE_PAGE_BY
    paginate_orphans = settings.BASE_ORPHANS

    def get_ordering(self):
        ordering = super(IndexView, self).get_ordering()
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-views','-update_date','-id')
        return ordering