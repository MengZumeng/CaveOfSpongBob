from django.db import models
from django.conf import settings
from django.shortcuts import reverse
import markdown
import emoji


# Create your models here.

class TestClass(models.Model):
    context = models.CharField('测试内容',max_length=200)

    class Meta:
        verbose_name = '测试类'
        verbose_name_plural = verbose_name
        ordering = ['-id']


# 文章关键词，用来作为SEO中keywords
class Keyword(models.Model):
    name = models.CharField('文章关键词', max_length=20)

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField('描述',max_length=240,default=settings.SITE_DESCRIPTION,
                                   help_text='用来作为SEO中description,长度参考SEO标准')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'slug': self.slug})

    def get_article_list(self):
        '''返回当前标签下所有发表的文章列表'''
        return Article.objects.filter(tags=self)

# 文章分类
class Category(models.Model):
    name = models.CharField('文章分类', max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField('描述',max_length=240,default=settings.SITE_DESCRIPTION,
                                   help_text='用来作为SEO中description,长度参考SEO标准')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def get_article_list(self):
        return Article.objects.filter(category=self)

# 文章
class Article(models.Model):
    IMG_LINK = settings.DEFAULT_IMG_LINL
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者',on_delete=models.SET(''))
    title = models.CharField(max_length=150, verbose_name='文章标题')
    summary = models.TextField('文章摘要', max_length=230, default='文章摘要等同于网页description内容，请务必填写...')
    body = models.TextField(verbose_name='文章内容')
    img_link = models.CharField('图片地址', default=IMG_LINK, max_length=255)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    views = models.IntegerField('阅览量', default=0)
    slug = models.SlugField(unique=True)
    is_top = models.BooleanField('置顶', default=False)

    category = models.ForeignKey(Category, verbose_name='文章分类',on_delete=models.SET(''))
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    keywords = models.ManyToManyField(Keyword,verbose_name='文章关键词',help_text='文章关键词，用来作为SEO中keywords，最好使用长尾词，3-4个足够')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_pre(self):
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()

class AboutBlog(models.Model):
    body = models.TextField(verbose_name='About 内容')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'About'

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])


# 幻灯片
class Carousel(models.Model):
    number = models.IntegerField('编号',help_text='编号决定图片播放的顺序，图片不要多于5张')
    title = models.CharField('标题',max_length=20,blank=True,null=True,help_text='标题可以为空')
    content = models.CharField('描述',max_length=80)
    img_url = models.CharField('图片地址',max_length=200)
    url = models.CharField('跳转链接',max_length=200,default='#',help_text='图片跳转的超链接，默认#表示不跳转')

    class Meta:
        verbose_name = '图片轮播'
        verbose_name_plural = verbose_name
        ordering = ['number','id']

    def __str__(self):
        return self.content[:25]



