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
        content = request.POST['commentContent']
        if content:
            Comment.objects.create(author=request.user, post=Post.objects.get(slug=kwargs['slug']), content=content)
        else:
            context['error_message'] = 'The comment can\'t be empty'

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {
        'banner_page_title' : Post.objects.get(slug=kwargs['slug']),
        'page_location' : 'home / post',
        'post' : Post.objects.get(slug=kwargs['slug']),
        'author_description' : Profile.objects.get(user=Post.objects.get(slug=kwargs['slug']).author).description
        }
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        forms.instance.post = Post.objects.get(slug=kwargs['slug'])
        return super().form_valid(form)
