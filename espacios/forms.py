# -*- encoding: utf-8 -*-
from django import forms
from espacios.models import Espacios,ZonaCamara,EspaciosEmbebido


class EspaciosForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = Espacios
        fields = '__all__'
        # exclude = ('id_cliente',)

    def __init__(self, *args, **kwargs):
        super(EspaciosForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)


class ZonaCamarasForm(forms.ModelForm):
    

    class Meta:
        model = ZonaCamara
        fields =  '__all__'
        #fields =  ('nombre_zona_camara','nro_personas',)
        #exclude = ('id_cliente',)

class EspaciosEmbebidoForm(forms.ModelForm):
    

    class Meta:
        model = EspaciosEmbebido        
        fields =  ('descripcion','zonas_camara',)
       
         




