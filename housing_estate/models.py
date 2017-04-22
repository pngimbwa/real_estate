from django.db import models
from geoposition.fields import GeopositionField


PAYMENT_MODE_CHOICES = (
    ('3Months', 'Three Months'),
    ('6Months', 'Six Months'),
    ('1Year', 'One Year'),
)
'''
HOME_TYPE_CHOICES = (
    ('House', 'House'),
    ('Apartment', 'Apartment'),
    ('Hostel', 'Hostel'),
)
'''
def get_image_path(instance, filename):
    #return os.path.join(BASE_DIR, "assets_env","media_root", filename)
    return os.path.join('upload',filename)

class HouseSpecification(models.Model):
    HasGypsum = models.BooleanField(default=False)
    HasAluminiumWindows = models.BooleanField(default=False)
    HasTiles = models.BooleanField(default=False)
    Rented = models.BooleanField(default=False)
    SelfContained = models.BooleanField(default=False)
    VanishedRoom = models.BooleanField(default=False)
    HasWater = models.BooleanField(default=False)
    HasElectricity = models.BooleanField(default=False)

    class Meta:
        abstract = True

'''
class HomeType(models.Model):
    homeID = models.CharField(primary_key =True,max_length=5)
    hometype = models.CharField(choices=PAYMENT_MODE_CHOICES, max_length=10)

    def __str__(self):
        return self.hometype

'''

HOME_TYPE=(
    ('House','House'),
    ('Apartment','Apartment'),
    ('Hostel','Hostel')
    )

class Address(models.Model):
    HouseNo = models.CharField(primary_key=True, max_length=20)
    #Hometype = models.CharField(choices=HOME_TYPE,max_length=20)
    StreetName = models.CharField(max_length=30)
    position = GeopositionField()

    def __str__(self):
        return (self.HouseNo)


class Owner(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50, blank=True, null=True)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.FirstName,self.LastName)


class Hostel(models.Model):
    HostelName = models.CharField(max_length=30)
    NumOfRooms = models.IntegerField("Number of Rooms")
    available_rooms = models.IntegerField('Available rooms',blank=True, null=True)
    address = models.ForeignKey(Address)
    owner = models.ForeignKey(Owner)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.HostelName)


class HostelRoom(HouseSpecification):
    RoomNumber = models.IntegerField("Room Number")
    Price = models.FloatField()
    RoomSize = models.FloatField()
    RoomPaymentMode = models.CharField(choices=PAYMENT_MODE_CHOICES, max_length=10)
    hostel = models.ForeignKey(Hostel)
    Roomavalaibility = models.BooleanField(default=False)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.RoomNumber)

class Compound(models.Model):
    CompoundName = models.CharField(max_length=20)
    NoOfUnits = models.IntegerField()
    owner = models.ForeignKey(Owner)
    address = models.ForeignKey(Address)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.CompoundName)


class Apartment(HouseSpecification):
    ApartmentName = models.CharField(max_length=15)
    NoOfRooms = models.IntegerField()
    ApartmentSize = models.FloatField()
    compound = models.ForeignKey(Compound)
    ApartmentPaymentMode = models.CharField(choices=PAYMENT_MODE_CHOICES, max_length=10)
    price = models.FloatField()
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.ApartmentName)


class House(HouseSpecification):
    HouseName = models.CharField(max_length=20)
    NoOfRooms = models.IntegerField()
    HouseSize = models.FloatField()
    owner = models.ForeignKey(Owner)
    address = models.ForeignKey(Address)
    price = models.FloatField()
    HousePaymentMode = models.CharField(choices=PAYMENT_MODE_CHOICES, max_length=10)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.HouseName)
