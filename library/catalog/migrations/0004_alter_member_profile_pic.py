# Generated by Django 4.2.10 on 2024-02-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_stacks_wanttoread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic'),
        ),
    ]