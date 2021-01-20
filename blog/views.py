from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Comment
from users.models import Profile
from taggit.models import Tag
from .forms import PostCreateForm
from users.mixins import IsSuperuserOrStaffMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Post.tags.most_common()[:8]
        context['banner_page_title'] = 'Blog'
        context['page_location'] = 'home / blog'
        context['tags'] = tags
        return context


class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Post.tags.most_common()[:8]
        context['banner_page_title'] = 'Blog'
        context['page_location'] = 'home / blog'
        context['tags'] = tags
        return context

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return Post.objects.filter(tags=tag)


class PostDetailView(DetailView):
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        content, replied_comment = request.POST['commentContent'], None
        if content:
            comment_id = request.POST.get('commentId')
            post = Post.objects.get(slug=kwargs['slug'])
            if comment_id:
                replied_comment = Comment.objects.get(id=comment_id)
            Comment.objects.create(author=request.user, post=post, reply=replied_comment, content=content)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        post = Post.objects.get(slug=kwargs['slug'])
        try:
            context['previous_post'] = Post.objects.get(id=post.id - 1)
        except:
            context['previous_post_none'] = 'No previous post'
        try:
            context['next_post'] = Post.objects.get(id=post.id + 1)
        except:
            context['next_post_none'] = 'No next post'
        context['banner_page_title'] = post
        context['page_location'] = 'home / post'
        context['post'] = post
        context['comments'] = Comment.objects.filter(post=post, reply=None)
        context['author_description'] = Profile.objects.get(user=post.author).description
        return context


class PostCreateView(LoginRequiredMixin, IsSuperuserOrStaffMixin, CreateView):
    template_name = 'blog/add_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = ['title', 'content', 'category', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'users/post.html'
    success_url = reverse_lazy('blog')

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)
