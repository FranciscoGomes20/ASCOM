# Generated by Django 4.0.1 on 2022-01-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_requestion_applicant_alter_requestion_assigned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestion',
            name='anexo',
            field=models.ImageField(blank=True, null=True, upload_to='App\\img_upload', verbose_name='Imagem'),
        ),
    ]
