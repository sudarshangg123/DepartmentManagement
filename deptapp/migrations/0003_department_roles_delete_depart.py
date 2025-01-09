# Generated by Django 5.1.4 on 2025-01-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deptapp', '0002_depart_delete_department_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Depart',
        ),
    ]
