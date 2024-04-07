# Generated by Django 5.0.3 on 2024-04-07 21:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0001_initial'),
        ('animal', '0003_animal_adotado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackadocao',
            name='adocao',
        ),
        migrations.RemoveField(
            model_name='formularioadocao',
            name='adotante',
        ),
        migrations.RemoveField(
            model_name='perfiladotante',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='statusadocao',
            name='animal',
        ),
        migrations.CreateModel(
            name='SolicitacaoAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('endereco', models.CharField(max_length=100)),
                ('outros_animais', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Aprovada', 'Aprovada'), ('Recusada', 'Recusada')], default='Pendente', max_length=20)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
                ('aprovado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitação de adoção',
                'verbose_name_plural': 'Solicitações de adoção',
                'ordering': ['-data'],
            },
        ),
        migrations.DeleteModel(
            name='Adocao',
        ),
        migrations.DeleteModel(
            name='FeedbackAdocao',
        ),
        migrations.DeleteModel(
            name='FormularioAdocao',
        ),
        migrations.DeleteModel(
            name='PerfilAdotante',
        ),
        migrations.DeleteModel(
            name='StatusAdocao',
        ),
    ]
