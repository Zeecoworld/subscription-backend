# Generated by Django 4.0.4 on 2022-05-24 12:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0007_alter_membership_duration_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentScreenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='reference_code',
        ),
        migrations.AddField(
            model_name='usermembership',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='membership',
            name='duration_period',
            field=models.DateField(default=datetime.date(2022, 6, 23)),
        ),
        migrations.DeleteModel(
            name='PaymentHistory',
        ),
    ]
