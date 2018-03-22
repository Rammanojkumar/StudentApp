# Generated by Django 2.0 on 2018-03-15 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('courseId', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('rankId', models.AutoField(primary_key=True, serialize=False)),
                ('Desc', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.AutoField(primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=60)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CourseDetails')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Score', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rankId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Rank')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Student')),
            ],
        ),
    ]
