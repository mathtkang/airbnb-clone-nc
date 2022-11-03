# Generated by Django 4.1.2 on 2022-11-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
                ('experience', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='experiences.experience')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=140)),
                ('experience', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='experiences.experience')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
