# Generated by Django 4.0.4 on 2022-05-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_alter_membership_duration_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Free', 'Free'), ('Jasper', 'Jasper'), ('Onynx', 'Onynx'), ('Obsidian', 'Obsidian'), ('Pearl', 'Pearl'), ('Ruby', 'Ruby'), ('Sapphire', 'Sapphire'), ('Topaz', 'Topaz'), ('Opal', 'Opal'), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Diamond', 'Diamond')], default='Free', max_length=40),
        ),
    ]
