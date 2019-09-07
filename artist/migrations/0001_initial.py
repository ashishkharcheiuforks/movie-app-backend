# Generated by Django 2.2.4 on 2019-09-07 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Job Category',
                'verbose_name_plural': 'Job Categories',
                'db_table': 'job_categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Seo link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.JobCategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'db_table': 'jobs',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('slug', models.SlugField(unique=True, verbose_name='Seo link')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('jobs', models.ManyToManyField(to='artist.Job', verbose_name='Jobs')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
                'db_table': 'artists',
                'ordering': ('-id',),
            },
        ),
    ]
