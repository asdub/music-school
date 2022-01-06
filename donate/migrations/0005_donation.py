# Generated by Django 3.2.9 on 2021-12-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_donateindexpage_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_id', models.CharField(editable=False, max_length=32)),
                ('status', models.CharField(editable=False, max_length=32)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(max_length=254)),
                ('donation_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('receipt', models.URLField(editable=False)),
            ],
        ),
    ]
