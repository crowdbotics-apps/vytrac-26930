# Generated by Django 3.2.4 on 2021-07-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('messages', models.JSONField(blank=True, max_length=30, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='deadline')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('priority', models.CharField(choices=[('00_low', 'Low'), ('10_normal', 'Normal'), ('20_high', 'High'), ('30_critical', 'Critical'), ('40_blocker', 'Blocker')], default='10_normal', max_length=20)),
            ],
            options={
                'get_latest_by': 'date_created',
            },
        ),
        migrations.CreateModel(
            name='AlertRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, help_text='if this blanck I will moniter all objects', null=True)),
                ('filter', models.CharField(blank=True, help_text='example: "oxgyn__lt=80"', max_length=999, null=True)),
                ('field_value', models.CharField(blank=True, help_text='If field value equal/gte/contains... then I will alert you', max_length=999, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('priority', models.CharField(choices=[('00_low', 'Low'), ('10_normal', 'Normal'), ('20_high', 'High'), ('30_critical', 'Critical'), ('40_blocker', 'Blocker')], default='10_normal', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AllDataStr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=999, null=True)),
                ('codename', models.CharField(blank=True, max_length=999, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeeAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SeenBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
