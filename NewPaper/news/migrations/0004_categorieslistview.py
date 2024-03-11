# Generated by Django 5.0.2 on 2024-03-11 18:07

import django.db.models.deletion
import django.views.generic.list
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_subscribers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesListView',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.post')),
            ],
            bases=('news.post', django.views.generic.list.ListView),
        ),
    ]
