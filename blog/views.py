from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from users.models import Profile


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_page_title'] = 'Blog'
        context['page_location'] = 'home / blog'
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post.html'

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['banner_page_title'] = Post.objects.get(slug=slug)
        context['page_location'] = 'home / post'
        context['post'] = Post.objects.get(slug=slug)
        context['author_description'] = Profile.objects.get(
            user=request.user).description
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        return context
