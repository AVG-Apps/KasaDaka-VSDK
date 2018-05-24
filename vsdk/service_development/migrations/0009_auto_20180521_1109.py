# Generated by Django 2.0.4 on 2018-05-21 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_development', '0008_auto_20180521_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('image_url', models.URLField(null=True)),
                ('voice_label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service_development.VoiceLabel')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('voice_label', models.ManyToManyField(blank=True, to='service_development.VoiceLabel')),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='fertilizers',
            field=models.ManyToManyField(to='service_development.Fertilizer'),
        ),
        migrations.AddField(
            model_name='crop',
            name='tutorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service_development.Tutorials'),
            preserve_default=False,
        ),
    ]
