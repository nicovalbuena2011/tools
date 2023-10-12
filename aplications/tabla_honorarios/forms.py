from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class HonorariosForm(forms.Form):

    ## Las opciones deben ser una lista de tuplas para que el select renga su clave y valor para renderizar.



    perfiles = [(1, 'Auxiliar'), (2, 'Técnico'), (3, 'Profesional'), (4, 'Profesional Especializado')]



    select_perfil = forms.ChoiceField(label = 'Perfil Profesional', choices = perfiles,widget = forms.Select(attrs = {'class': 'form-control'}))

    input_experiencia = forms.CharField(label = 'Ingrese la experiencia en meses',widget = forms.TextInput(attrs = {'class': 'form-control'}) )


    ## Validacion de la experiencia:

    def clean(self):

        cleaned_data = super().clean()

        select_pefil = cleaned_data.get('select_perfil')
        input_experiencia = cleaned_data.get('input_experiencia')

        if select_pefil == '1' and (int(input_experiencia) > 18 or int(input_experiencia) < 6):
           self.add_error('input_experiencia','Un Auxiliar no puede tener esa experiencia, recuerde que la experiencia para Auxiliares es de 6 a 18 meses.')


        return cleaned_data