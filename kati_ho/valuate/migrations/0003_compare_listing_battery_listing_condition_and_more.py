# Generated by Django 4.1.5 on 2023-02-24 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('valuate', '0002_auto_20230213_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('fc', models.CharField(max_length=10)),
                ('pc', models.CharField(max_length=10)),
                ('display', models.FloatField()),
                ('res', models.CharField(max_length=10)),
                ('Model', models.CharField(max_length=100)),
                ('battery', models.IntegerField()),
                ('Link', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='battery',
            field=models.IntegerField(default=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='condition',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(default='Apple', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='res',
            field=models.CharField(default='720x1080', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='size',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(default='sanatan', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
