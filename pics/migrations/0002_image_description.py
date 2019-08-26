
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
