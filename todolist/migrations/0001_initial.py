# Generated by Django 2.2.3 on 2019-07-16 07:07

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
            name='TodoListItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todoTitle', models.CharField(max_length=50)),
                ('todoDescription', models.CharField(max_length=400)),
                ('todoDateTime', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(choices=[('red', 'High'), ('orange', 'Medium'), ('green', 'Low')], default='green', max_length=10)),
                ('testing', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
