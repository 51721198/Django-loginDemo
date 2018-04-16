# Generated by Django 2.0.4 on 2018-04-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostpitalNumber', models.IntegerField()),
                ('hospitalName', models.CharField(max_length=30)),
                ('hospitalPhone', models.CharField(max_length=15)),
                ('hospitalAddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LicenseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumberId', models.IntegerField()),
                ('sourceNumber', models.CharField(max_length=30)),
                ('createDate', models.DateTimeField()),
                ('expiredDate', models.DateTimeField()),
                ('encryptedNumber', models.CharField(max_length=100)),
                ('hospitalNumber', models.IntegerField()),
                ('licenseState', models.IntegerField()),
                ('keyId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RSAKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyId', models.IntegerField()),
                ('privateKey', models.BinaryField()),
                ('publicKey', models.BinaryField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='userinformation',
            options={'ordering': ['id']},
        ),
    ]
