# Generated by Django 4.2.2 on 2024-02-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_customer_c_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
