# Generated by Django 3.2.3 on 2021-05-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greatsoftapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.CharField(blank=True, choices=[('Website', 'Website'), ('mobile', 'mobile'), ('Design', 'Design'), ('TGBot', 'TGBot')], max_length=50, null=True),
        ),
    ]
