# Generated by Django 2.2.4 on 2020-04-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_exchange', '0003_auto_20200430_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
