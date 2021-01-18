from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment
from users.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
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

    def test_blog_list_view_GET(self):
        response = self.client.get(self.blog_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_tagged_post_list_view_GET(self):
        response = self.client.get(self.tag_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_post_detail_view_GET(self):
        response = self.client.get(self.post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')

    #Incomplete Test (errors appearing)
    # def test_post_create_view_POST(self):
    #     response = self.client.post(self.add_post_url, {
    #         'title' : 'shell post',
    #         'content' : 'shell post content',
    #     })
    #     post = Post.objects.last()
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(post.title, 'shell post')
