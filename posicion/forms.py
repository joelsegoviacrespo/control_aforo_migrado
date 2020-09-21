# -*- encoding: utf-8 -*-
from django import forms
from posicion.models import Posicion,PosicionEmbebido
from instalacion.models import Instalacion


class PosicionForm(forms.ModelForm):
    
    
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    numero_cliente = forms.CharField(widget=forms.HiddenInput, required=False, initial="")
    cliente_nif = forms.ChoiceField()
        
    
    class Meta:
        model = Posicion
        fields =  '__all__'
        #exclude = ('nombre_archivo_verde','nombre_archivo_ambar','nombre_archivo_rojo','nombre_archivo_cerrado',)

    def __init__(self, *args, **kwargs):
        super(PosicionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            
               
         

        
class PosicionEmbebidoForm(forms.ModelForm):
    

    class Meta:
        model = PosicionEmbebido        
        fields =  ('posicion_reloj','color',)

  
                
         

