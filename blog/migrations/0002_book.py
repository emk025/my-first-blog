# Generated by Django 2.2.24 on 2021-12-08 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
