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
        'desde': 1148359,
        'hasta': 1515360,
        'exp-inicial': 6,
        'exp-final': 12
    },{
        'perfil': 'Auxiliar II',
        'desde': 1516436,
        'hasta': 1789804,
        'exp-inicial': 13,
        'exp-final': 18
    },{
        'perfil': 'Técnico I',
        'desde': 1790880,
        'hasta': 2067476,
        'exp-inicial': 0,
        'exp-final': 11
    },{
        'perfil': 'Técnico II',
        'desde': 2068553,
        'hasta': 2480756,
        'exp-inicial': 12,
        'exp-final': 18
    },{
        'perfil': 'Profesional I',
        'desde': 2481833,
        'hasta': 3170633,
        'exp-inicial': 0,
        'exp-final': 12
    },{
        'perfil': 'Profesional II',
        'desde': 3171709,
        'hasta': 3859433,
        'exp-inicial': 13,
        'exp-final': 24
    },{
        'perfil': 'Profesional Especializado I',
        'desde': 3860509,
        'hasta': 4685993,
        'exp-inicial': 0,
        'exp-final': 12
    },{
        'perfil': 'Profesional Especializado II',
        'desde': 4572750,
        'hasta': 5653541,
        'exp-inicial': 13,
        'exp-final': 24
    },{
        'perfil': 'Profesional Especializado III',
        'desde': 5516700,
        'hasta': 6341265,
        'exp-inicial': 25,
        'exp-final': 48
    }]


    for obj in honorarios_mensuales:
        if obj['perfil'] == perfil:
            salario = np.interp(experiencia,[obj['exp-inicial'],obj['exp-final']],[obj['desde'],obj['hasta']])
            locale.setlocale(locale.LC_ALL, '')
            sueldo_formateado = locale.format_string("%.2f", salario, grouping=True)

            return sueldo_formateado

