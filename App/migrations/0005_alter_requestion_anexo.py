# Generated by Django 4.0.1 on 2022-01-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_requestion_applicant_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestion',
            name='anexo',
            field=models.ImageField(upload_to='App\\img_upload', verbose_name='Imagem'),
        ),
    ]
