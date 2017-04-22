from .models import Address, Apartment, Compound, Hostel, HostelRoom, House, HouseSpecification, Owner
from django import template
from django.core.context_processors import csrf
from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from itertools import chain



def list_addresses(request):
    retrieved_address = Address.objects.all()
    json_models = serializers.serialize("json", retrieved_address)
    return HttpResponse(json_models, content_type="application/javascript")




def get_home(request,housetype,bed_number,min_price,max_price):
    #if housetype =='Hostel':
    available_rooms = bed_number
    home_instance = HostelRoom.objects.filter(hostel__available_rooms=available_rooms,Price__gte=min_price,Price__lte=max_price)
    json_models =  serializers.serialize('json',home_instance)
    return HttpResponse(json_models, content_type="application/javascript")
