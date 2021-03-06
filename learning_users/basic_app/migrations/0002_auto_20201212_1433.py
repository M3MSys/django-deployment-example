# Generated by Django 3.1.3 on 2020-12-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portofolio_site',
            new_name='portfolio_site',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='basic_app/profile_pics'),
        ),
    ]
