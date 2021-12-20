# Generated by Django 3.2.9 on 2021-12-19 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0025_homepage_pathways'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='pathways',
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway1_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway2_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway3_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway4_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway5_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway6',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway6_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway7',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway7_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway8',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway8_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway9',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pathway9_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button Link'),
        ),
    ]
