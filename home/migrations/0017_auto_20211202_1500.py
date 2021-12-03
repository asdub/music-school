# Generated by Django 3.2.9 on 2021-12-02 15:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0016_alter_homepage_support_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='contact_address',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='contact_phone',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='googlemaps_embed',
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_phone', models.CharField(max_length=100, null=True)),
                ('contact_email', models.CharField(max_length=100, null=True)),
                ('contact_address', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('googlemaps_embed', models.CharField(max_length=350, null=True)),
                ('logo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Site logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]