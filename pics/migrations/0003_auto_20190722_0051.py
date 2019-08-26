
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_image_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='photo',
            new_name='image',
        ),
    ]
