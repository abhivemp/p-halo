# Generated by Django 3.2.5 on 2021-07-28 14:34

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
            name='hacker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=60)),
                ('education', models.CharField(choices=[('High School/Secondary School', 'High School/Secondary School'), ('University (Undergrad)', 'University (Undergrad)'), ("University (Master's/Doctoral)", "University (Master's/Doctoral)")], max_length=60)),
                ('major', models.CharField(default='other', max_length=60)),
                ('hacker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hacker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
