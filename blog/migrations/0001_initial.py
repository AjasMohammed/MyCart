# Generated by Django 4.1.1 on 2022-10-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=5000)),
                ('head1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
