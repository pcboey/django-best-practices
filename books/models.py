from django.db import models
from django.core.urlresolvers import reverse

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse('publisher-detail', kwargs={'pk': self.pk})

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __unicode__(self): 
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self): 
        return self.title
