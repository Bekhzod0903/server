# Generated by Django 5.0.6 on 2024-05-26 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0003_alter_roadsigns_audio_alter_roadsigns_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadsigns',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='signs.category'),
            preserve_default=False,
        ),
    ]
