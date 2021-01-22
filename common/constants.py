from django.utils.translation import ugettext_lazy as _


error_messages = {
    'first_name' : _('First name can contain only letters'),
    'last_name' : _('Last name can contain only letters'),
}

help_texts = {
    'email' : _('Enter a valid email, ex: name@example.com'),
    'only_letters' : _('Enter just letters'),
    'date' : _('Enter a valid date, ex: 2001-04-23'),
    'phone_number' : _('Enter prefix + number, ex: +40123456789'),
    'description' : _('Description can contain any characters'),
    'name' : _('Enter letters, numbers or special characters'),
    'amount' : _('Enter a number with maxim 10 digits and 3 decimals'),
}

messages = {
    'email_exists' : 'This email is already subscribed in our system',
    'email_subscribed' : 'Your email was subscribed in our system, you\'ll hear from us as soon as possible !',
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
    'contact_path' : 'home / Contact',
    'dashboard_title' : 'Dashboard',
    'profile_title' : 'Profile',
}
