# Generated by Django 5.0.3 on 2024-04-01 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0002_animal_historico_saude'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_adocao', models.DateField()),
                ('adocao_bemsucedida', models.BooleanField(default=False)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('adocao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adocao.adocao')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilAdotante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FormularioAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('experiencia_anterior', models.BooleanField()),
                ('outros_animais', models.BooleanField()),
                ('adotante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.perfiladotante')),
            ],
        ),
        migrations.AddField(
            model_name='adocao',
            name='adotante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.perfiladotante'),
        ),
        migrations.CreateModel(
            name='StatusAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
        ),
    ]