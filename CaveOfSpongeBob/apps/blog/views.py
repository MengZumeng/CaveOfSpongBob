from .models import Article, Tag, Category, Timeline, Silian,TestClass
from django.views import generic
from django.conf import settings
from django.shortcuts import render

# Create your views here.
class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = settings.BASE_PAGE_BY
    paginate_orphans = settings.BASE_ORPHANS

    def get_ordering(self):
        ordering = super().get_ordering()
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-views','-update_date','-id')
        return ordering


class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get_object(self):
        obj = super(DetailView, self).get_object()
        # 设置浏览量增加时间判断,同一篇文章两次浏览超过2小时才重新统计阅览量,作者浏览忽略
        u = self.request.user
        ses = self.request.session
        the_key = 'is_read_{}'.format(obj.id)
        is_read_time = ses.get(the_key)
        if u != obj.author:
            if not is_read_time:
                obj.update_views()
                ses[the_key] = time.time()
            else:
                now_time = time.time()
                t = now_time - is_read_time
                if t > 7200:
                    obj.update_views()
                    ses[the_key] = time.time()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        obj.body = md.convert(obj.body)
        obj.toc = md.toc
        return obj