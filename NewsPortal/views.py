from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from xml.dom import ValidationErr
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import NewsFilter
from NewsPortal.models import Post
from .forms import NewsForm


# Create your views here.


class ListNews(ListView):
    model = Post
    ordering = 'pub_time'
    template_name = 'news/news.html'
    context_object_name = 'news'
    paginate_by = 2


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news'




class SearchListView(ListNews):
    template_name = 'news/search.html'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.create_Post',)
    form_class = NewsForm
    model = Post
    template_name = 'news/news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
            path_info = self.request.META['PATH_INFO']
            if path_info == '/news/create/':
                post.post_type = 'NS'
            elif path_info == '/post/create/':
                post.post_type = 'PT'

        post.save()
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_Post',)
    form_class = NewsForm
    model = Post
    template_name = 'news/news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
            pub_path = self.request.META['PATH_INFO']
            pub_type = pub_path.split('/')[1]
            if pub_type == 'post' and self.object.post_type == 'PT' or pub_type == 'news' and self.object.post_type == 'NS':
                return super().form_valid(form)
            else:
                raise ValidationErr(f'Редактирование невозможно: путь {pub_path} не соответствует типу публикации {self.object.post_type}')


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('NewsPortal.delete_Post',)
    model = Post
    context_object_name = 'news'
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        if self.request.method == 'POST':
            pub_path = self.request.META['PATH_INFO']
            pub_type = pub_path.split('/')[1]
            if pub_type == 'post' and self.object.post_type == 'PT' or pub_type == 'news' and self.object.post_type == 'NS':
                return super().form_valid(form)
            else:
                raise ValidationErr(f'Удаление невозможно: путь {pub_path} не соответствует типу публикации {self.object.post_type}')
