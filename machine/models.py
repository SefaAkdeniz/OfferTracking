from django.db import models

# Create your models here.

TYPE_CHOICES = (
    (1, 'CNC Talaşlı İmalat Teknolojileri'),
    (2, 'Saç İşleme Makinaları')
)

COMPANY_CHOICES = (
    (1, 'A Markası'),
    (2, 'B Markası')
)

class Machine(models.Model):
    machine_name = models.CharField(max_length=100, verbose_name="Tezgah Adı")
    machine_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, verbose_name="Tezgah Tipi",default=1)
    machine_company = models.PositiveSmallIntegerField(choices=COMPANY_CHOICES, verbose_name="Tezgah Markası",default=1)


    def __str__(self):
        return self.machine_name

    class Meta:
        verbose_name = 'Tezgah'
        verbose_name_plural = 'Tezgahlar'


    