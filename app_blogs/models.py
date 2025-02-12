
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel

UserModel = get_user_model()

# Create your models here.
class BlogsCategoryModel(BaseModel):
    objects = True
    title = models.CharField(max_length=128,verbose_name=_('title'))
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('parent')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = 'blog categories'


class BlogsTagModel(BaseModel):
    objects = True
    title = models.CharField(max_length=128,verbose_name=_('title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog tag')
        verbose_name_plural = _('blog tages')



class BlogsAuthorModel(BaseModel):
    first_name = models.CharField(max_length=128,verbose_name=_('first_name'))
    last_name = models.CharField(max_length=128,verbose_name=_('last_name'))
    avatar = models.ImageField(upload_to="blogs/authors/",verbose_name=_('avatar'))

    @property
    def get_full_name(self):
        return self.__repr__()

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


    def __repr__(self):
        return f'{self.first_name}{self.last_name}'

    class Meta:
        verbose_name = _('blog author')
        verbose_name_plural = _('blog authors')




class BlogsModel(BaseModel):
    objects = True
    images = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=128)
    description = models.TextField(verbose_name=_('description'))

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    author = models.ManyToManyField(BlogsAuthorModel,related_name="blogs",verbose_name=_('author'))
    categories = models.ManyToManyField(BlogsCategoryModel,related_name="blogs",verbose_name=_('categories'))
    tags = models.ManyToManyField(BlogsTagModel,related_name="tags",verbose_name=_('tags'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'



class BlogsCommentModel(BaseModel):
    comment = models.CharField(max_length=128,verbose_name=_('title'))
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='blog_comments',
        verbose_name=_('user')
    )
    blog = models.ForeignKey(
        BlogsModel,
        on_delete=models.CASCADE,
        related_name='blog_comments',
        verbose_name=_('user')
    )



    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('blog comment')
        verbose_name_plural = _('blog comments')
