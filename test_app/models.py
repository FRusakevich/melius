from django.db import models


# Create your models here.
class Zayavka(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, related_name='rel_zayavka')

    def __str__(self):
        return self.title


class Contract(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True),

    def __str__(self):
        return self.title


class Tovar(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    zayavka = models.ForeignKey(Zayavka, on_delete=models.CASCADE, related_name='rel_tovar')
    proizvoditel = models.OneToOneField('Proizvoditel', on_delete=models.CASCADE, related_name='rel_proizdodotel')

    def __str__(self):
        return self.title


class Proizvoditel(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title
