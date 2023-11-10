from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils.text import slugify



class Category(models.Model):
    category_name = models.CharField(max_length=200)
    body = RichTextField()
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img  = models.FileField(upload_to="Category/Img",blank=True,null=True,verbose_name="Изображения Поста")
    
    class Meta:
        verbose_name = "Категирия"
        verbose_name_plural = "Категирии"
        db_table = 'posts_category'

    def __str__(self):
        return self.category_name

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Имя Поста")
    head_body = RichTextField()
    head_img = models.FileField(upload_to='Post/Img',blank=True,null=True,verbose_name="Изображения верхенего поста")
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='post')
    price = models.IntegerField(default=0)
    count_views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ('-publish',)

    def __str__(self):
        return "Дата: {}, Названия: {}".format(self.created,self.title)


    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

class NumberUser(models.Model):
    number_us = models.CharField(max_length=30,verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Дата: {}, Названия: {}".format(self.created,self.number_us)

class modelEmail(models.Model):
    name = models.CharField(max_length=200,verbose_name='Имя Пользователя')
    tel  = models.CharField(max_length=30,verbose_name='Номер')
    question = models.CharField(max_length=300,verbose_name='Тектс')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Дата: {}, Названия: {}".format(self.created,self.name)

class PostCountViews(models.Model):
    sesId = models.CharField(max_length=150,db_index=True)
    postId = models.ForeignKey(Post,blank=True,null=True,default=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.sesId)