from django.db import models

# Create your models here.

TYPE_CHOICES = (
    (1, 'İş Makinesi Üreticileri'),
    (2, 'İstif Makineleri Üreticileri'),
    (3, 'Tarım Makinaları Üreticileri'),
    (4, 'Hidrolik Pnömatikçiler'),  
    (5, 'Diğer'),
)

CONTACT_CHOICES = (
    (1, 'Refarans Tavsiyesi'),
    (2, 'Sosyal Medya'),
    (3, 'Mağaza Ziyareti'),
    (4, 'E-Mail'),
    (5, 'Telefon Araması'),
    (6, 'Diğer')
)

CITY_CHOICES = (
    (6, 'ANKARA'),
    (34, 'İSTANBUL'),
    (35, 'İZMİR'),
    (17, 'ÇANAKKALE'),  
)

class Customer(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Firma Adı",unique=True)
    company_type = models.PositiveSmallIntegerField( choices=TYPE_CHOICES, verbose_name="Firma İş Alanı",default=1)
    company_phone = models.CharField(max_length=11, verbose_name="Firma Telefon Numarası",default="0216")
    company_city = models.PositiveSmallIntegerField( choices=CITY_CHOICES, verbose_name="Konum",default=34)
    company_adress = models.TextField(verbose_name="Adres")
    first_contact = models.PositiveSmallIntegerField(choices=CONTACT_CHOICES,verbose_name="İlk İletişim",default=1)
    related_person_name1= models.CharField(max_length=100, verbose_name="1.İlgili Kişi Adı")
    related_person_title1= models.CharField(max_length=100, verbose_name="1.İlgili Ünvanı")
    related_person_phone1= models.CharField(max_length=11, verbose_name="1.İlgili Kişi Cep Telefon Numarası",default="05")
    related_person_mail1= models.CharField(max_length=100, verbose_name="1.İlgili Kişi E-Posta Adresi")
    related_person_name2= models.CharField(max_length=100, verbose_name="2.İlgili Kişi Adı",blank=True)
    related_person_title2= models.CharField(max_length=100, verbose_name="2.İlgili Ünvanı",blank=True)
    related_person_phone2= models.CharField(max_length=11, verbose_name="2.İlgili Kişi Cep Telefon Numarası",blank=True)
    related_person_mail2= models.CharField(max_length=100, verbose_name="2.İlgili Kişi E-Posta Adresi",blank=True)
    first_contact_date = models.DateTimeField(auto_now_add=True, verbose_name="İlk İlişki Tarihi",blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Müşteri'
        verbose_name_plural = 'Müşteriler'
