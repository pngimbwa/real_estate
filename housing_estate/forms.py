from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import admin
from django.forms import Select
from django.contrib.admin.widgets import AdminTimeWidget
from django.utils.safestring import mark_safe
from django.forms.widgets import TextInput
from django.conf import settings


from .models import Address, Apartment, Compound, Hostel, HostelRoom, House, Owner, HouseSpecification


class AddressForm(forms.ModelForm):
        class Meta:
                model = Address
                fields = '__all__'

        def __init__(self, *args, **kwargs):
                super(AddressForm, self).__init__(*args, **kwargs)
                self.fields['HouseNo'].widget.attrs['class'] = 'form-control'
                self.fields['StreetName'].widget.attrs['class'] = 'form-control' 
                self.fields['position'].widget.attrs['class'] = 'form-control'
                
                
class ApartmentForm(forms.ModelForm):
        class Meta:
                model = Apartment
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(ApartmentForm, self).__init__(*args, **kwargs)
                self.fields['ApartmentName'].widget.attrs['class'] = 'form-control'
                self.fields['NoOfRooms'].widget.attrs['class'] = 'form-control' 
                self.fields['ApartmentSize'].widget.attrs['class'] = 'form-control'
                self.fields['compound'].widget.attrs['class'] = 'form-control'
                self.fields['ApartmentPaymentMode'].widget.attrs['class'] = 'form-control' 
                self.fields['price'].widget.attrs['class'] = 'form-control'
                self.fields['picture'].widget.attrs['class'] = 'form-control'
                
                          
class CompoundForm(forms.ModelForm):
        class Meta:
                model = Compound
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(CompoundForm, self).__init__(*args, **kwargs)
                self.fields['CompoundName'].widget.attrs['class'] = 'form-control'
                self.fields['NoOfUnits'].widget.attrs['class'] = 'form-control' 
                self.fields['owner'].widget.attrs['class'] = 'form-control'
                self.fields['address'].widget.attrs['class'] = 'form-control'
                self.fields['picture'].widget.attrs['class'] = 'form-control'
                
                

class HostelForm(forms.ModelForm):
        class Meta:
                model = Hostel
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(HostelForm, self).__init__(*args, **kwargs)
                self.fields['HostelName'].widget.attrs['class'] = 'form-control'
                self.fields['NumOfRooms'].widget.attrs['class'] = 'form-control' 
                self.fields['address'].widget.attrs['class'] = 'form-control'
                self.fields['owner'].widget.attrs['class'] = 'form-control'
                self.fields['picture'].widget.attrs['class'] = 'form-control' 



class HostelRoomForm(forms.ModelForm):
        class Meta:
                model = HostelRoom
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(HostelRoomForm, self).__init__(*args, **kwargs)
                self.fields['RoomNumber'].widget.attrs['class'] = 'form-control'
                self.fields['Price'].widget.attrs['class'] = 'form-control' 
                self.fields['RoomSize'].widget.attrs['class'] = 'form-control'
                self.fields['RoomPaymentMode'].widget.attrs['class'] = 'form-control'
                self.fields['hostel'].widget.attrs['class'] = 'form-control'
                self.fields['picture'].widget.attrs['class'] = 'form-control' 



class HouseForm(forms.ModelForm):
        class Meta:
                model = House
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(HouseForm, self).__init__(*args, **kwargs)
                self.fields['HouseName'].widget.attrs['class'] = 'form-control'
                self.fields['NoOfRooms'].widget.attrs['class'] = 'form-control' 
                self.fields['HouseSize'].widget.attrs['class'] = 'form-control'
                self.fields['owner'].widget.attrs['class'] = 'form-control'
                self.fields['address'].widget.attrs['class'] = 'form-control'
                self.fields['price'].widget.attrs['class'] = 'form-control'
                self.fields['HousePaymentMode'].widget.attrs['class'] = 'form-control'
                self.fields['picture'].widget.attrs['class'] = 'form-control'
                
                

class OwnerForm(forms.ModelForm):
        class Meta:
                model = Owner
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(OwnerForm, self).__init__(*args, **kwargs)
                self.fields['FirstName'].widget.attrs['class'] = 'form-control'
                self.fields['MiddleName'].widget.attrs['class'] = 'form-control' 
                self.fields['LastName'].widget.attrs['class'] = 'form-control'
                self.fields['Email'].widget.attrs['class'] = 'form-control'
                self.fields['Phone'].widget.attrs['class'] = 'form-control'




HOUSE_TYPE_CHOICES=(
        ('','Choose..'),
        ('House','House'),
        ('Apartment','Apartment'),
        ('Hostel','Hostel')
)

BEDS_CHOICES=(
        ('','Choose..'),
        (1,'1+'),
        (2,'2+'),
        (3,'3+'),
        (4,'4+'),
        (5,'5+'),
        (6,'6+')
)

MIN_PRICE_CHOICES_RANGE=(
        ('','Choose..'),
        (0,'0'),
        (30000,'30,000'),
        (50000,'50,000'),
        (70000,'70,000'),
        (100000,'100,000'),
        (150000,'150,000')
)

MAX_PRICE_CHOICES_RANGE=(
        ('','Choose..'),
        (30000,'30,000'),
        (50000,'50,000'),
        (70000,'70,000'),
        (100000,'100,000'),
        (150000,'150,000'),
        (250000,'250,000')
)

YEAR_BUILT_MIN=(
        ('','Choose..'),
        (1990,'1990'),
        (2000,'2000')
)

YEAR_BUILT_MAX=(
        ('','Choose..'),
        (2000,'2000'),
        (2017,'2017')

)

CHOICES=[
        ('HasGypsum','Gypsum'),
        ('HasAluminiumWindows','Aluminium Windows'),
        ('HasTiles','Tiles'),
        ('SelfContained','Self Contained'),
        ('HasElectricity','Electricity'),
        ('VanishedRoom','Vanished Room'),
        ('HasGypsum','Gypsum'),
        ('HasAluminiumWindows','Aluminium Windows')
        ]



class EstateForm(forms.Form):
        housetype =  forms.ChoiceField(choices = HOUSE_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        beds =  forms.ChoiceField(choices = BEDS_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        min_price =  forms.ChoiceField(choices = MIN_PRICE_CHOICES_RANGE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        max_price =  forms.ChoiceField(choices = MAX_PRICE_CHOICES_RANGE, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        
        #year_built_min =  forms.ChoiceField(choices = YEAR_BUILT_MIN, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        #year_built_max =  forms.ChoiceField(choices = YEAR_BUILT_MAX, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        rooms = forms.ChoiceField(choices = BEDS_CHOICES, widget=forms.Select(attrs={'class': 'form-control seleckpicker'}))
        choices = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
'''
class HouseSpecificationForm(forms.ModelForm):
        class Meta:
                model = HouseSpecification
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super(OwnerForm, self).__init__(*args, **kwargs)
                self.fields['HasGypsum'].widget.attrs['class'] = 'form-control'
                self.fields['HasAluminiumWindows'].widget.attrs['class'] = 'form-control' 
                self.fields['HasTiles'].widget.attrs['class'] = 'form-control'
                self.fields['Rented'].widget.attrs['class'] = 'form-control'
                self.fields['SelfContained'].widget.attrs['class'] = 'form-control'
                self.fields['VanishedRoom'].widget.attrs['class'] = 'form-control'
                self.fields['HasElectricity'].widget.attrs['class'] = 'form-control' 

'''