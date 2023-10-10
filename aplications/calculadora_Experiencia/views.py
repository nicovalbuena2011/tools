import datetime
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.urls import reverse
from .forms import (
    InputForm,
    DateForm
)
from django.views.generic import (
    TemplateView,
)

def form2(request):

    form = InputForm()
    num_contratos = None

    if 'select_contratos' in request.GET:
        num_contratos = request.GET['select_contratos']
    elif 'select_contratos' in request.POST:
        num_contratos = request.POST['select_contratos']


    formset = formset_factory(DateForm,extra= int(num_contratos) ,max_num=10)
    if request.method == 'POST':



        set = formset(request.POST)

        if set.is_valid():
            for form in set:
                # Accede a los valores de los campos del formulario
                fecha_inicio = form.cleaned_data['fecha_inicio']
                fecha_fin = form.cleaned_data['fecha_fin']

                # Haz algo con los valores, como imprimirlos
                print(f'Fecha de inicio: {fecha_inicio}')
                print(f'Fecha de fin: {fecha_fin}')
        


        return render(request, 'experiencia/form2.html',{
            'formset':formset,
            'numero_contratos':num_contratos,
            'form':form
        })
    else:
        return render(request, 'experiencia/form2.html',{
            'formset':formset,
            'numero_contratos':num_contratos,
            'form':form
        })



def inicio(request):

    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            numero_contratos = form.cleaned_data['select_contratos']
            return render(request, "experiencia/form2.html", {
                'numero_contratos': int(numero_contratos),
                'form':form,
            })
    else:
        form = InputForm()

        return render(request, "experiencia/form2.html", {
            'form':form
        })


    
"""
    Vistas definitivas

"""



def welcome(request):

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            

            key = form.cleaned_data['select_contratos']

            # Paso el dato a la sesion             
            request.session['key'] = key

            return redirect('calculadora:validar-experiencia')
            
            


    else:


        form = InputForm()

        return render(request, "experiencia/numContratos.html" , {
            'form': form
        })
    
    
def validar_experiencia(request):

    # Recupero el dato de la sesion
    key = request.session.get('key', None)
    
    MyFormset = formset_factory(DateForm,extra= int(key) ,max_num=10)
    if request.method == 'POST':
        print('entre1')
        formset = MyFormset(request.POST)

        if formset.is_valid():
            print('valido')
            recopiled_data = []
            

            for form in formset:
                data = form.cleaned_data

                recopiled_data.append(data['fecha_fin'] - data['fecha_inicio'])

            print(recopiled_data)

            
            # sumar aca una unidad para que cuente los dias actuales #

            total_days = sum( td.days + 1 for td in recopiled_data )
            print(total_days)
            meses, dias = divmod(total_days,30)
            print(f'la persona tiene de experiencia: meses: {meses}, dias {dias}')


            return render(request, 'experiencia/validator.html',{
                'formset': formset,
                'meses': meses,
                'dias': dias,
                'errors':False
            })
        
        else:
            return render(request, 'experiencia/validator.html',{
                'formset': formset,
                'errors' : True
            })

    else:
        print('entre2')
        # formset = formset_factory(DateForm,extra= int(key) ,max_num=10)
        return render(request, 'experiencia/validator.html',{
            'formset': MyFormset
        })


    # return render(request, "experiencia/numContratos.html")

