# Generated by Django 4.0.1 on 2022-05-09 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_etudiant_photoprofil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='bio',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='telephone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='universite',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='ville',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investisseur',
            name='telephone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investisseur',
            name='ville',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
