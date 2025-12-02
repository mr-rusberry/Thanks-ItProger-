from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anouns', max_length=250)
    article = models.TextField('Article')
    date = models.DateTimeField('date')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'