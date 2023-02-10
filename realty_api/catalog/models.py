from django.db import models
from .services import real_estate_dir_path


class RealEstate(models.Model):
    # Choices
    DEAL_TYPE = (
        ("B", "Buy"),
        ("R", "Rent"),
    )

    # Fields
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to=real_estate_dir_path)
    cost = models.FloatField('Cost')
    year_build = models.IntegerField('Year build')
    parking_space_count = models.IntegerField('Parking space count')
    parking_detail = models.CharField('Parking detail', max_length=50)
    deal_type = models.CharField('Deal type', choices=DEAL_TYPE, max_length=1)

    def __str__(self):
        return self.location.address

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

class Location(models.Model):
    address = models.CharField('Address', max_length=150)
    state = models.CharField('State', max_length=50)
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')
    real_estate = models.OneToOneField(RealEstate, on_delete=models.CASCADE, related_name='location')


class Option(models.Model):
    value = models.CharField('Value', max_length=100)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, related_name='options')
