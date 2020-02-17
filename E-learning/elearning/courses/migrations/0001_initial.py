# Generated by Django 2.2.1 on 2019-07-02 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('grouping', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SID', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='my_img_avatar')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TID', models.IntegerField()),
                ('Tname', models.CharField(max_length=50)),
                ('Tfamily', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='my_img_avatar')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Tcourse', models.ManyToManyField(blank=True, to='courses.Course')),
                ('Tstudent', models.ManyToManyField(blank=True, to='courses.Student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Cteacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, to='courses.Student'),
        ),
    ]