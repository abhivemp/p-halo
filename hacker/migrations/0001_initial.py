# Generated by Django 4.0.1 on 2022-02-14 18:13

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
            name='HackerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(choices=[('High School/Secondary School', 'High School/Secondary School'), ('University (Undergrad)', 'University (Undergrad)'), ("University (Master's/Doctoral)", "University (Master's/Doctoral)")], default='other', max_length=60)),
                ('major', models.CharField(choices=[('Accounting', 'Accounting'), ('Biology', 'Biology'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Business Administration', 'Business Administration'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Communications', 'Communications'), ('Computer Engineering', 'Computer Engineering'), ('Computer Science', 'Computer Science'), ('Construction Management', 'Construction Management'), ('Cybersecurity', 'Cybersecurity'), ('Economics', 'Economics'), ('Education', 'Education'), ('Electronics Engineering', 'Electronics Engineering'), ('English', 'English'), ('Finance', 'Finance'), ('Game Design', 'Game Design'), ('Health Informatics', 'Health Informatics'), ('Industrial Engineering', 'Industrial Engineering'), ('Interactive Multimedia', 'Interactive Multimedia'), ('Information Technology', 'Information Technology'), ('Liberal Arts', 'Liberal Arts'), ('Management', 'Management'), ('Management Information Systems', 'Management Information Systems'), ('Marketing', 'Marketing'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Nuclear Engineering', 'Nuclear Engineering'), ('Nursing', 'Nursing'), ('Petroleum Engineering', 'Petroleum Engineering'), ('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Public Administration', 'Public Administration'), ('Software Engineering', 'Software Engineering')], default='other', max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hacker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hacker',
            },
        ),
    ]
