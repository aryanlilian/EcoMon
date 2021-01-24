from django.utils.translation import ugettext_lazy as _
from users.models import Income, Spending


income_obj = Income
spending_obj = Spending


error_messages = {
    'first_name' : _('First name can contain only letters.'),
    'last_name' : _('Last name can contain only letters.'),
    'required' : _('This field is required!'),
    'post_title_size' : _('The length of the title can\'t be longer then 200 characters')
}

email_activation = {
    'subject' : 'Email activation!',
    'body' : 'Hello, We\'ve sent you this email because you need to activate your account from EcoMon, copy this number:\n',
}

help_texts = {
    'email' : _('Required. A valid email (e.g name@example.com).'),
    'only_letters' : _('Required. 100 characters or fewer. Letters only.'),
    'phone_number' : _('Required. prefix + number (e.g. +40123456789).'),
    'date' : _('Required. A valid date (e.g. 2001-04-23), YYYY/MM/DD.'),
    'profile_description' : _('Optional. Letters, digits and/or @/./+/-/_ only.'),
    'obj_name' : _('Required. 100 characters or fewer. Letters, digits and/or @/./+/-/_ only.'),
    'obj_amount' : _('Required. 10 digits or fewer and/or 3 decimals or fewer.'),
    'post_title' : _('Required. 200 characters or fewer. Letters, digits and/or @/./+/-/_ only.'),
    'any_character' : _('Required. Letters, digits and/or special characters'),
}

messages = {
    'email_exists' : 'This email is already subscribed in our system!',
    'email_subscribed' : 'Your email was subscribed in our system, you\'ll hear from us as soon as possible!',
    'email_received' : 'We\'ve received your email, you\'ll hear from us very soon!',
    'fail_sent_email' : 'Something didn\'t work, please try later!',
}

template_titles = {
    'blog_title' : 'Blog',
    'blog_path' : 'home / blog',
    'post_path' : 'home / post',
    'no_previous_post' : 'No previous post',
    'no_next_post' : 'No next post',
    'about_title' : 'About Us',
    'about_path' : 'home / about',
    'contact_title' : 'Contact',
    'contact_path' : 'home / contact',
    'dashboard_title' : 'Dashboard',
    'profile_title' : 'Profile',
}
