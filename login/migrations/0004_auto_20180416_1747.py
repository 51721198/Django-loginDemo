# Generated by Django 2.0.4 on 2018-04-16 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20180416_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licensedetail',
            old_name='createDate',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='licensedetail',
            old_name='encryptedNumber',
            new_name='encrypted_number',
        ),
        migrations.RenameField(
            model_name='licensedetail',
            old_name='expiredDate',
            new_name='expired_date',
        ),
        migrations.RenameField(
            model_name='licensedetail',
            old_name='hospitalNumber',
            new_name='hospital_number',
        ),
        migrations.RenameField(
            model_name='licensedetail',
            old_name='keyId',
            new_name='key_id',
        ),
        migrations.RenameField(
            model_name='licensedetail',
            old_name='licenseState',
            new_name='license_state',
        ),
        migrations.RenameField(
            model_name='licensedetail',
            old_name='serialNumberId',
            new_name='serial_number_id',
        ),
        migrations.RenameField(
            model_name='licensedetail',
            old_name='sourceNumber',
            new_name='source_number',
        ),
        migrations.RenameField(
            model_name='rsakey',
            old_name='keyId',
            new_name='key_id',
        ),
        migrations.RenameField(
            model_name='rsakey',
            old_name='privateKey',
            new_name='private_key',
        ),
        migrations.RenameField(
            model_name='rsakey',
            old_name='publicKey',
            new_name='public_key',
        ),
    ]
