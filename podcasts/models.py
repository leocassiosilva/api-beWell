from django.db import models


class Podcast(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_podcast")
    nome = models.CharField(max_length=100)
    url = models.TextField()
    descricao = models.TextField(blank=True, null=True)
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)
    id_usuario = models.ForeignKey("accounts.CustomUsuario", on_delete=models.CASCADE, db_column="id_usuario")

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = "podcast"
        managed = True