# Generated by Django 4.2.7 on 2023-11-09 12:48

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('body', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='Category/Img', verbose_name='Изображения Поста')),
            ],
            options={
                'verbose_name': 'Категирия',
                'verbose_name_plural': 'Категирии',
                'db_table': 'posts_category',
            },
        ),
        migrations.CreateModel(
            name='modelEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя Пользователя')),
                ('tel', models.CharField(max_length=30, verbose_name='Номер')),
                ('question', models.CharField(max_length=300, verbose_name='Тектс')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NumberUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_us', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Имя Поста')),
                ('head_body', ckeditor.fields.RichTextField()),
                ('head_img', models.FileField(blank=True, null=True, upload_to='Post/Img', verbose_name='Изображения верхенего поста')),
                ('body', ckeditor.fields.RichTextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=0)),
                ('count_views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='apps.category')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='PostCountViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sesId', models.CharField(db_index=True, max_length=150)),
                ('postId', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.post')),
            ],
        ),
    ]
