# Generated by Django 4.1.1 on 2022-10-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cont_head0',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='cont_head1',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='cont_head2',
            field=models.TextField(default='', max_length=5000),
        ),
    ]
