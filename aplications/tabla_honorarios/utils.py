import locale
import numpy as np
"""
1. Funcion que clasifica el perfil profesional y da el sueldo.

"""

def validar_pefil(perfil, experiencia):

    
    
    if perfil == '1':
        if experiencia >=6 and experiencia <=12:
            return {
                'profile':'Auxiliar I',
                'salario':validar_honorario('Auxiliar I',experiencia)
            }
        else:
            return {
                'profile':'Auxiliar II',
                'salario':validar_honorario('Auxiliar II',experiencia)
            }

    elif perfil == '2':

        if experiencia >=0 and experiencia <=11:
            return {
                'profile':'Técnico I',
                'salario':validar_honorario('Técnico I',experiencia)
            } 
        else:
            return {
                'profile':'Técnico II',
                'salario':validar_honorario('Técnico II',experiencia)
            }

    elif perfil == '3':

        if experiencia >=0 and experiencia <=12:
            return {
                'profile':'Profesional I',
                'salario':validar_honorario('Profesional I',experiencia)
            } 
        else:
            return {
                'profile':'Profesional II',
                'salario':validar_honorario('Profesional II',experiencia)
            } 

    else:
        if experiencia >=0 and experiencia <=12:
            return {
                'profile':'Profesional Especializado I',
                'salario':validar_honorario('Profesional Especializado I',experiencia)
            } 
        
        elif experiencia >=13 and experiencia <=24:
            return {
                'profile':'Profesional Especializado II',
                'salario':validar_honorario('Profesional Especializado II',experiencia)
            } 
        
        else:
            return {
                'profile':'Profesional Especializado III',
                'salario':validar_honorario('Profesional Especializado III',experiencia)
            }
        

def validar_honorario(perfil,experiencia):
    
    honorarios_mensuales = [{
        'perfil': 'Auxiliar I',
        'desde': 1400000,
        'hasta': 1600000,
        'exp-inicial': 6,
        'exp-final': 12
    },{
        'perfil': 'Auxiliar II',
        'desde': 1600001,
        'hasta': 1900000,
        'exp-inicial': 13,
        'exp-final': 18
    },{
        'perfil': 'Técnico I',
        'desde': 1900001,
        'hasta': 2200000,
        'exp-inicial': 0,
        'exp-final': 11
    },{
        'perfil': 'Técnico II',
        'desde': 2200001,
        'hasta': 2600000,
        'exp-inicial': 12,
        'exp-final': 18
    },{
        'perfil': 'Profesional I',
        'desde': 2600001,
        'hasta': 3300000,
        'exp-inicial': 0,
        'exp-final': 12
    },{
        'perfil': 'Profesional II',
        'desde': 3300001,
        'hasta': 4000000,
        'exp-inicial': 13,
        'exp-final': 24
    },{
        'perfil': 'Profesional Especializado I',
        'desde': 4000001,
        'hasta': 5000000,
        'exp-inicial': 0,
        'exp-final': 12
    },{
        'perfil': 'Profesional Especializado II',
        'desde': 5000001,
        'hasta': 6000000,
        'exp-inicial': 13,
        'exp-final': 24
    },{
        'perfil': 'Profesional Especializado III',
        'desde': 6000001,
        'hasta': 6700000,
        'exp-inicial': 25,
        'exp-final': 48
    }]


    for obj in honorarios_mensuales:
        if obj['perfil'] == perfil:
            salario = np.interp(experiencia,[obj['exp-inicial'],obj['exp-final']],[obj['desde'],obj['hasta']])
            locale.setlocale(locale.LC_ALL, '')
            sueldo_formateado = locale.format_string("%.2f", salario, grouping=True)

            return sueldo_formateado

