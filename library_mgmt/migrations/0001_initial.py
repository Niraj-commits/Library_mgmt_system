# Generated by Django 5.1.6 on 2025-02-16 04:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('author', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('borrowed', 'borrowed'), ('returned', 'returned'), ('none', 'none')], default='none', max_length=50)),
                ('genre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='library_mgmt.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='library_mgmt.book')),
                ('member', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='library_mgmt.member')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('cancelled', 'cancelled')], default='pending', max_length=50)),
                ('book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='library_mgmt.book')),
                ('member', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='library_mgmt.member')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='library_mgmt.book')),
                ('member', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='library_mgmt.member')),
            ],
        ),
    ]
