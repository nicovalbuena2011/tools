from django.shortcuts import render
from .forms import (
    HonorariosForm
)

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = HonorariosForm(request.POST)
        if form.is_valid():

            form = HonorariosForm()
            return render(request,'tabla_honorarios/home.html',{
                'form': form
            })
        
        else:

            print(f'errores: {form.errors}' )
            return render(request,'tabla_honorarios/home.html',{
                'form': form
            })


    else:

        form = HonorariosForm()
        return render(request,'tabla_honorarios/home.html',{
            'form': form
        })
