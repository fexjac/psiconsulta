from django.db import models
from django.utils.datetime_safe import datetime

# artist = models.ForeignKey(Musician)


class Pessoa(models.Model):
    nome = models.Charfield(max_length=60, null=False)
    telefone = models.CharField(max_length=11, null=False)
    endereco = models.Charfield(max_length=60, null=False)
    email = models.EmailField()
    data_cadastro = models.DateTimeField(default=datetime.now(), null=False)


class Terapeuta(models.Model):
    pessoa = models.ForeignKey(Pessoa, null=False)
    sexo = models.CharField()
    cpf = models.CharField(max_length=11, null=False)
    registro_profissional = models.CharField(max_length=10, null=False)


class Paciente(models.Model):
    pessoa = models.ForeignKey(Pessoa, null=False)
    pessoa_terapeuta = models.ForeignKey(Pessoa, null=False)
    pessoa_responsavel = models.ForeignKey(Pessoa, null=False)
    pessoa_profissional = models.ForeignKey(Pessoa)
    sexo = models.CharField()
    cpf = models.CharField(max_length=11, null=False)
    data_nascimento = models.datetime(null=False)
    baba = models.BooleanField()
    baba_telefone = models.CharField(max_length=11)
    escola_creche = models.BooleanField()
    escola_creche_telefone = models.CharField(max_length=11)


class Responsavel(models.Model):
    pessoa = models.ForeignKey(Pessoa, null=False)
    pessoa_paciente = models.ForeignKey(Pessoa, null=False)
    contato_profissional = models.CharField(max_length=11)


class Profissional(models.Model):
    pessoa = models.ForeignKey(Pessoa, null=False)
    pessoa_paciente = models.ForeignKey(Pessoa, null=False)
    local_atendimento = models.CharField(max_length=50)
    registro_profissional = models.CharField(max_length=10)


class Especialidade(models.Model):
    descricao = models.CharField(max_length=30, null=False)
