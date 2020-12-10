from django.db import models
from users.models import User
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

class Post(models.Model):

    class PostCategory(models.TextChoices):
        FAMILY = 'FAMILY', _('Family')
        BUSSINESS = 'BUSSINESS', _('Bussiness')
        MWRKETING = 'MARKETING', _('Marketing')
        SPENDINGS = 'SPENDINGS', _('Spendings')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Post\'s Title'), max_length=200, unique=True)
    content = models.TextField(_('Posts\'s Content'))
    category = models.CharField(_('Post\'s Category'), max_length=9, choices=PostCategory.choices, default=PostCategory.BUSSINESS)
    slug = models.SlugField(_('Slug'), max_length=200, blank=True, null=False, unique=True)
    tags = TaggableManager(_('Tags'))
    published_date = models.DateTimeField(_('Published Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
