# Generated by Django 2.2.1 on 2019-07-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Screen Name')),
                ('my_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
    ]
