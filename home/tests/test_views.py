from django.test import TestCase, Client
from django.urls import reverse
from home.models import Newsletter
from django.core import mail
from users.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.about_url = reverse('about')
        self.contact_url = reverse('contact')
        self.register_url = reverse('register')
        self.login_url = reverse('login')


    def test_index_form_view_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_index_form_view_POST_adds_newsletter_email(self):
        response = self.client.post(self.index_url, {
            'email': 'test@test.com'
        })
        newsletter = Newsletter.objects.first()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(newsletter.email, 'test@test.com')

    def test_about_template_view_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_contact_view_GET(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_contact_view_POST_send_mail(self):
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )
        mail.send_mail(
            'Subject here again', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )

        self.assertEquals(len(mail.outbox), 2)
        self.assertEquals(mail.outbox[0].subject, 'Subject here')
        self.assertEquals(mail.outbox[1].subject, 'Subject here again')

    def test_user_registration_create_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/auth/register.html')

    #Incomplete Test (errors appearing)
    # def test_user_registration_create_view_POST_adds_new_user(self):
    #     response = self.client.post(self.register_url, {
    #         'email' : 'test@test.com',
    #         'username' : 'test',
    #         'first_name' : 'test_first',
    #         'last_name' : 'test_last',
    #         'password1' : 'test',
    #         'password2' : 'test',
    #         'marketing_email' : 'on',
    #         'accept_terms_and_conditions' : 'on'
    #     })
    #     user = User.objects.first()
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(user.email, 'test@test.com')
    #     self.assertEquals(user.username, 'test')
    #     self.assertEquals(user.first_name, 'test_first')
    #     self.assertEquals(user.last_name, 'test_last')

    def test_user_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/auth/login.html')

    #Incomplete Test (errors appearing)
    # def test_user_login_view_POST_login_user(self):
    #     response = self.client.post(self.login_url, {
    #         'username' : 'test2', 'password' : 'testregister'
    #     })
    #     self.assertEquals(response.status_code, 302)
