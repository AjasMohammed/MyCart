# Generated by Django 4.1.1 on 2022-10-22 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_cont_head0_blogpost_cont_head1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='thumnail',
            new_name='thumbnail',
        ),
    ]