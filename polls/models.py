import datetime
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class Post(models.Model):
    post_header = models.CharField(default = '',max_length = 100)
    posts_auftor_name = models.CharField(default = '',max_length=100)
    post_text = models.TextField(max_length = 200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.post_header

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Image(models.Model):
     images_post = models.ForeignKey(Post)
     image = models.ImageField(upload_to ='images/',
                               height_field = "height_field",
                               width_field = "width_field")
     height_field = models.IntegerField(default = 0)
     width_field = models.IntegerField(default = 0)

class File(models.Model):
    files_pots = models.ForeignKey(Post)
    file = models.FileField(upload_to = '/files/')


class Comment(models.Model):
    comments_post = models.ForeignKey(Post)
    comment_text = models.TextField(verbose_name='Текст коментаря')
    comments_auftor_name = models.CharField(default = '',max_length=100)
    comment_pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_text

# Create your models here.