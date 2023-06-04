from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField('Titre', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,  blank=True, null=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    update_date = models.DateField(auto_now= datetime.today())
    content = models.TextField('Contenue', blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='blog')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
         if not self.slug:
             self.slug = slugify(self.title)
         super().save(*args, **kwargs)

    @property
    def publier(self):
        if self.published:
            return 'publieé'
        return 'Non publié'

