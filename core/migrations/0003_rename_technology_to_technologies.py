from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='technology',
            new_name='technologies',
        ),
    ]
