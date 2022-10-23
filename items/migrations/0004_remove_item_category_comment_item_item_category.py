# Generated by Django 4.1.2 on 2022-10-23 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='items.item'),
        ),
        migrations.AddField(
            model_name='item',
            name='Category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items.category'),
        ),
    ]
