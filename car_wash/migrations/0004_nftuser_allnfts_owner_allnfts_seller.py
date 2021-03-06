# Generated by Django 4.0.3 on 2022-05-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0003_allnfts_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nftuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('profile_pic', models.CharField(max_length=255)),
                ('cover_pic', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='allnfts',
            name='owner',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='allnfts',
            name='seller',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
