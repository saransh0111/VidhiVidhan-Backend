# Generated by Django 4.2.7 on 2023-11-26 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
        ('users', '0002_otpmanager_customer_created_customer_modified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pandit',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this instance was created.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this instance was modified.')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='user/profile/')),
                ('price', models.FloatField(max_length=100, verbose_name='pandit price for booking')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShopOwner',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this instance was created.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this instance was modified.')),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='user/profile/')),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('is_new', models.BooleanField(default=False, help_text='detail of this user is not filled')),
                ('pin_code', models.CharField(blank=True, max_length=100, null=True)),
                ('products', models.ManyToManyField(to='market.products', verbose_name='shop products')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
