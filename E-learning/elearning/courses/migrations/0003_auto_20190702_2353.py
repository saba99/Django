# Generated by Django 2.2.1 on 2019-07-02 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190702_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='Cteacher',
        ),
        migrations.CreateModel(
            name='Quize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textquestion', models.CharField(max_length=255)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Quize')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('content', models.TextField(blank=True, null=True)),
                ('Lcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textanswer', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False, verbose_name='correctAnswer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Question')),
            ],
        ),
    ]
