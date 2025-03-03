# Generated by Django 5.1.5 on 2025-01-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0002_blogscommentmodel_blog_alter_blogsmodel_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsauthormodel',
            name='first_name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='blogsauthormodel',
            name='first_name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='blogsauthormodel',
            name='first_name_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='blogsauthormodel',
            name='last_name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='blogsauthormodel',
            name='last_name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='blogsauthormodel',
            name='last_name_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='blogscategorymodel',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogscategorymodel',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogscategorymodel',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogscommentmodel',
            name='comment_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogscommentmodel',
            name='comment_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogscommentmodel',
            name='comment_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogsmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='blogsmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='blogsmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='blogsmodel',
            name='title_en',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blogsmodel',
            name='title_ru',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blogsmodel',
            name='title_uz',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='blogstagmodel',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogstagmodel',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogstagmodel',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='title'),
        ),
    ]
