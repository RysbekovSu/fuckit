# Generated by Django 4.1.3 on 2022-12-07 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser2', '0003_news_description_news_image_news_published_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='description',
        ),
        migrations.RemoveField(
            model_name='news',
            name='published_data',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_text',
        ),
    ]