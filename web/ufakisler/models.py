from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    writer = models.CharField(max_length=50)
    date = models.DateTimeField('date published')


    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    writer = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    date = models.DateTimeField('date published')

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title
