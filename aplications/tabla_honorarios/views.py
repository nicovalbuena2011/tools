from django.shortcuts import render, redirect
from .utils import (validar_pefil)
from .forms import (
    HonorariosForm
)

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = HonorariosForm(request.POST)
        if form.is_valid():

            datos_formulario = form.cleaned_data
            # print(f'datos: {datos_formulario}')

            request.session['perfil'] = datos_formulario['select_perfil']
            request.session['experiencia'] = datos_formulario['input_experiencia']
            
            return redirect('honorarios:validar')

            # return render(request,'tabla_honorarios/home.html',{
            #     'form': form
            # })
        
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
    
def validarHonorarios(request):
    
    experiencia = request.session.get('experiencia',None)
    perfil = request.session.get('perfil',None)


    

    # print(f'{type(experiencia)}, {type(perfil)}')

    if request.method == 'POST':
        pass

    else:
        
        sueldo = validar_pefil(perfil, int(experiencia))
        
        return render(request,'tabla_honorarios/validar.html',{
            'perfil': sueldo['profile'],
            'salario': sueldo['salario'],
            'experiencia' : experiencia
        })

