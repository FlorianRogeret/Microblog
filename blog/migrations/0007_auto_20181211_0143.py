# Generated by Django 2.1.3 on 2018-12-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
