from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment
from users.models import User


class BaseTest(TestCase):

    def setUp(self):
        self.blog_url = reverse('blog')
        self.tag_url = reverse('tag', args=['test'])
        self.post_url = reverse('post', args=['test-post'])
        self.add_post_url = reverse('add-post')
        self.user = User.objects.create(
            username='testuser',
            email='test@test.com',
            first_name='test',
            last_name='test',
            password='test'
        )
        self.post = Post.objects.create(
            author=self.user,
            title='Test post',
            content='test content post',
        )
        self.post.tags.add('test')
        return super().setUp()

class TestBlogViews(BaseTest):

    def test_blog_list_view_GET(self):
        response = self.client.get(self.blog_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


class TestTaggetPostViews(BaseTest):

    def test_tagged_post_list_view_GET(self):
        response = self.client.get(self.tag_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


class TestPostDetailViews(BaseTest):

    def test_post_detail_view_GET(self):
        response = self.client.get(self.post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')


class TestPostCreateViews(BaseTest):

    pass
    #Incomplete Test(errors)
    # def test_post_create_view_POST(self):
    #     response = self.client.post(self.add_post_url, {
    #         'title' : 'testing post title',
    #         'content' : 'shell post content',
    #         'category' : 'FAMILY',
    #         'tags' : 'blog, test'
    #     }, format='text/html')
    #     post = Post.objects.filter(title='testing post title').first()
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(post.title, 'testing post title')
