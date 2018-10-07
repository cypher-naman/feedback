# Generated by Django 2.1.1 on 2018-10-01 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=120)),
                ('rollno', models.IntegerField()),
                ('Punctuality', models.IntegerField()),
                ('Subject_knowledge', models.IntegerField()),
                ('Behaviour', models.IntegerField()),
                ('Method_of_teaching', models.IntegerField()),
                ('Audibility', models.IntegerField()),
                ('Syllabus_coverage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Section'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Teacher'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='teacher_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Subject'),
        ),
    ]
