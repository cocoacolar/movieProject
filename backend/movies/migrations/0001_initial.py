# Generated by Django 3.2.3 on 2021-11-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=200)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]