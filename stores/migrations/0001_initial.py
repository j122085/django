# Generated by Django 2.0 on 2017-12-26 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('notes', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='menu_items', to='stores.Store'),
        ),
    ]
