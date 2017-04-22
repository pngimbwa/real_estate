from django.contrib import admin
from .models import Address, Apartment, Compound, Hostel, HostelRoom, House, Owner,HouseSpecification

'''
class HouseSpecificationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('HasGypsum','HasAluminiumWindows','HasTiles','Rented','SelfContained','VanishedRoom','HasWater','HasElectricity')
admin.site.register(HouseSpecification,HouseSpecificationAdmin)
'''

class AddressAdmin(admin.ModelAdmin):
    search_fields = ['HouseNo','StreetName']
    list_display = ('HouseNo','StreetName','position')
admin.site.register(Address,AddressAdmin)


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['FirstName','LastName']
    list_display = ('FirstName','MiddleName','LastName','Email','Phone')
admin.site.register(Owner,OwnerAdmin)


class HostelAdmin(admin.ModelAdmin):
    search_fields = ['HostelName','NumOfRooms']
    list_display = ('HostelName','NumOfRooms','available_rooms','address','owner','picture')
admin.site.register(Hostel,HostelAdmin)


class HostelRoomAdmin(admin.ModelAdmin):
    search_fields = ['RoomNumber','hostel__HostelName']
    list_display = ('RoomNumber','Roomavalaibility','Price','RoomSize','RoomPaymentMode','hostel','picture')
admin.site.register(HostelRoom,HostelRoomAdmin)


class CompoundAdmin(admin.ModelAdmin):
    search_fields = ['CompoundName','owner__FirstName']
    list_display = ('CompoundName','NoOfUnits','owner','address','picture')
admin.site.register(Compound,CompoundAdmin)


class ApartmentAdmin(admin.ModelAdmin):
    search_fields = ['ApartmentName']
    list_display = ('ApartmentName','NoOfRooms','ApartmentSize','compound','ApartmentPaymentMode','price','picture')
admin.site.register(Apartment,ApartmentAdmin)


class HouseAdmin(admin.ModelAdmin):
    search_fields = ['ApartmentName']
    list_display = ('HouseName','NoOfRooms','HouseSize','owner','address','price','HousePaymentMode','picture')
admin.site.register(House,HouseAdmin)
