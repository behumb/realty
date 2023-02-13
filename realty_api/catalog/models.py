from django.db import models
from .services import real_estate_dir_path


class PropertyType(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


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
    bedroom_count = models.PositiveIntegerField('Bedrooms')
    bathroom_count = models.PositiveIntegerField('Bathrooms')
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, related_name='real_estates')
    total_square = models.FloatField('Total square')
    living_square = models.FloatField('Living_square')
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
    city = models.CharField('City', max_length=50)
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')
    real_estate = models.OneToOneField(RealEstate, on_delete=models.CASCADE, related_name='location')
