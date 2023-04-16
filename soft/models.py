from django.db import models
from django.urls import reverse


class Divan(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    image = models.ImageField(upload_to="divan/", verbose_name='изображение', blank=True, null=True)
    cost = models.IntegerField(verbose_name='цена')
    about = models.TextField(verbose_name='описание')
    type = models.ForeignKey("Type", on_delete=models.SET_NULL, null=True, verbose_name='тип')
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('divan_', kwargs={'slug': self.slug})

    # def get_absolute_url(self):
    #     return f"/list/{self.slug}"

    class Meta:
        verbose_name = "Диван"
        verbose_name_plural = "Диваны"

    def get_absolute_url(self):
        return reverse("one_divan", args=[self.id])


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Orders(models.Model):

    divan = models.ForeignKey(Divan, related_name="orders", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()

    count = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.cost = self.count * self.divan.cost
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
