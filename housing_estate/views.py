from django.shortcuts import render

from .forms import EstateForm

def index(request):
    
    if request.method == 'POST': 
        estateform = EstateForm(request.POST)
      
        if estateform.is_valid():
            housetype = estateform.cleaned_data['housetype']

        else:
            context = {'estateform':EstateForm}
            return render (request,'index.html',locals())
      
    else:
        estateform = EstateForm()
        return render (request,'index.html',locals())
