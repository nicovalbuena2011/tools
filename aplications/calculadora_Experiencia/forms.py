from django import forms
from django.core.exceptions import ValidationError

class InputForm(forms.Form):

    ## Las opciones deben ser una lista de tuplas para que el select renga su clave y valor para renderizar.

    numbers =  [(i, str(i)) for i in range(1, 11)]
    """
        [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]
    
    """

    select_contratos = forms.ChoiceField(label = 'Numero contratos', choices = numbers,widget = forms.Select(attrs = {'class': 'form-control'}))


class DateForm(forms.Form):

    fecha_inicio = forms.DateField(required=True,widget = forms.DateInput(attrs = {'type' : 'date', 'class': 'form-control','required':'true'}))

    
    fecha_fin = forms.DateField(required=True, widget = forms.DateInput(attrs = {'type' : 'date', 'class': 'form-control','required':'true'}))

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise ValidationError('La fecha de inicio debe ser anterior a la fecha de finalización.')

        return cleaned_data


