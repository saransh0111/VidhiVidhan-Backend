# Generated by Django 4.2.7 on 2023-11-26 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTPManager',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this instance was created.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this instance was modified.')),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('otp', models.CharField(blank=True, max_length=4, null=True)),
                ('count', models.IntegerField(default=0, help_text='Count of OTP sent')),
            ],
            options={
                'verbose_name': 'otp_manager',
                'verbose_name_plural': 'otp managers',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='When this instance was created.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='When this instance was modified.'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this instance was created.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this instance was modified.')),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='user/profile/')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('is_new', models.BooleanField(default=False, help_text='detail of this user is not filled')),
                ('pin_code', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
