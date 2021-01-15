from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
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

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        content, replied_comment = request.POST['commentContent'], None
        if content:
            if request.POST.get('commentId'):
                replied_comment = Comment.objects.get(id=request.POST['commentId'])
            Comment.objects.create(author=request.user, post=Post.objects.get(slug=kwargs['slug']), reply=replied_comment, content=content)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        try:
            context['previous_post'] = Post.objects.get(id=Post.objects.get(slug=kwargs['slug']).id - 1)
        except:
            context['previous_post_none'] = 'No previous post'
        try:
            context['next_post'] = Post.objects.get(id=Post.objects.get(slug=kwargs['slug']).id + 1)
        except:
            context['next_post_none'] = 'No next post'
        context['banner_page_title'] = Post.objects.get(slug=kwargs['slug'])
        context['page_location'] = 'home / post'
        context['post'] = Post.objects.get(slug=kwargs['slug'])
        context['comments'] = Comment.objects.filter(post=Post.objects.get(slug=kwargs['slug']), reply=None)
        context['author_description'] = Profile.objects.get(user=Post.objects.get(slug=kwargs['slug']).author).description
        return context
