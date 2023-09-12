from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'st. {self.name}, {self.city.name}'

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'


class Shop(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    street = models.ForeignKey(Street, null=True, on_delete=models.SET_NULL)
    building = models.CharField(max_length=10)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f'{self.name}: st. {self.name}, building: {self.building}, {self.city.name}'

    @property
    def address(self):
        return f'st. {self.street.name}, {self.city.name}, building {self.building}'

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
