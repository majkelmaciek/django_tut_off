# Generated by Django 2.2.1 on 2019-05-11 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domena_WWW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField()),
                ('rating', models.IntegerField(default=0)),
                ('catergory', models.CharField(max_length=100)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alt_article_APP.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Alt_url_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField()),
                ('rating', models.IntegerField(default=0)),
                ('domena_WWW', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alt_article_APP.Domena_WWW')),
            ],
        ),
        migrations.CreateModel(
            name='Alt_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('alt_url_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alt_article_APP.Alt_url_link')),
                ('tag', models.ManyToManyField(to='alt_article_APP.Tag')),
            ],
        ),
    ]
