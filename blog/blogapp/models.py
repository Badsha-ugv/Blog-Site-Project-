from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    slug = models.SlugField(max_length=200,unique=True)
    blog_title = models.TextField(max_length=250,verbose_name='Title Here')
    blog_content = models.TextField(verbose_name='what is on your mind?')
    blog_image = models.ImageField(upload_to='blog_image',verbose_name='blog_image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment













