from django.shortcuts import render
from django.utils.translation.template import context_re
from django.views.generic import ListView, DetailView
from unicodedata import category

from app_blogs.models import *


# Create your views here.

class BlogsListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        blogs = BlogsModel.objects.all()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        if tag:
            blogs = blogs.filter(tag=tag)
        if category:
            blogs = blogs.filter(categories=category)

        return blogs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories']=BlogsCategoryModel.objects.all()
        context['recent_blogs']=BlogsModel.objects.order_by("-created_at")[:2]
        context['tags']=BlogsTagModel.objects.all()
        return context

class BlogDetailView(DetailView):
    model = BlogsModel
    template_name = 'blogs/blog-detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.object
        categories_id = blog.categories.values_list('id', flat=True)

        context['related_blogs'] = BlogsModel.objects.filter(
            categories__id__in=categories_id
        ).exclude(id=blog.id).distinct()[:3]

        return context
