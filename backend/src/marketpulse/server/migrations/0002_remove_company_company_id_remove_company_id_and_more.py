# Generated by Django 4.2.7 on 2023-12-10 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AddField(
            model_name='company',
            name='company_code',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='UserFavoritesCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='userfavoritescompany',
            constraint=models.UniqueConstraint(fields=('user', 'company'), name='favorite company uniqueness'),
        ),
    ]
