# Generated by Django 2.2.7 on 2019-11-15 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cacti', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cactus',
                'verbose_name_plural': 'Cacti',
            },
        ),
    ]
