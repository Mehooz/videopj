# Generated by Django 2.2.5 on 2019-09-06 07:49

from django.db import migrations, models
import django.db.models.deletion
import imagebkd.apiutils
import imagebkd.fileutils


class Migration(migrations.Migration):

    dependencies = [
        ('imagebkd', '0002_auto_20190904_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='input',
        ),
        migrations.CreateModel(
            name='InputFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.ImageField(upload_to=imagebkd.fileutils.determineUpload)),
                ('oper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagebkd.Operation')),
            ],
        ),
    ]
