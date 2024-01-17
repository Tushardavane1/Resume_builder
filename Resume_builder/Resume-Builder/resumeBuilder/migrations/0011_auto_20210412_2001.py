# Generated by Django 3.1.7 on 2021-04-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeBuilder', '0010_auto_20210412_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='currentYear',
            new_name='currentYear1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='degree',
            new_name='currentYear2',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='jobDescription',
            new_name='jobDescription1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='jobTitle',
            new_name='jobDescription2',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='projectTitle',
            new_name='university2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='jobEndDate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='jobStartDate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='projectDescription',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='projectEndDate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='projectStartDate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='stream',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='univPassingYear',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='univResult',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='univStartingYear',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='university',
        ),
        migrations.AddField(
            model_name='profile',
            name='degree1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='degree2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobDescription3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobDescription4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobDescription5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobEndDate1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobEndDate2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobEndDate3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobEndDate4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobEndDate5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobStartDate1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobStartDate2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobStartDate3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobStartDate4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobStartDate5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobTitle1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobTitle2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobTitle3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobTitle4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jobTitle5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectDescription1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectDescription2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectDescription3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectDescription4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectDescription5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectEndDate1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectEndDate2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectEndDate3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectEndDate4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectEndDate5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectStartDate1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectStartDate2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectStartDate3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectStartDate4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectStartDate5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectTitle1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectTitle2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectTitle3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectTitle4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='projectTitle5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='stream1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='stream2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='univPassingYear1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='univPassingYear2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='univResult1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='univResult2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='univStartingYear1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='univStartingYear2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='university1',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
