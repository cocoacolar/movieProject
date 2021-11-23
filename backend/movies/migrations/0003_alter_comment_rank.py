# Generated by Django 3.2.3 on 2021-11-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_comment_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rank',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=5),
        ),
    ]