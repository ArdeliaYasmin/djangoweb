from django.db import models

# Create your models here.

class Course(models.Model):
    nama        = models.CharField(max_length=50)
    dosen       = models.CharField(max_length=100)
    sks         = models.PositiveIntegerField()
    semester    = models.CharField(max_length=6, choices= [('Ganjil', 'Ganjil'),('Genap', 'Genap'),],default= 'Ganjil')
    tahun       = models.CharField(max_length=9,
        choices= [
    ('2020/2021', '2020/2021'),
    ('2021/2022', '2021/2022'),
    ('2022/2023', '2022/2023'),
    ],default='2019/2020')
    ruang        = models.CharField(max_length=20)
    deskripsi    = models.CharField(max_length=300)

    def __str__(self):
        return self.name
