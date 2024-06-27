# Generated by Django 5.0.6 on 2024-06-26 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_phonebookallocationtypes_default_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebooks',
            name='partner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.partners'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField()),
                ('amount', models.IntegerField()),
                ('status', models.CharField(null=True)),
                ('phonebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.phonebooks')),
            ],
        ),
    ]