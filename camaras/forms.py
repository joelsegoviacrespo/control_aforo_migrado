# -*- encoding: utf-8 -*-
from django import forms
from camaras.models import Camaras,ZonaCamara


class CamarasForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = Camaras
        fields = '__all__'
        # exclude = ('id_cliente',)

    def __init__(self, *args, **kwargs):
        super(CamarasForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)


class ZonaCamarasForm(forms.ModelForm):
    

    class Meta:
        model = ZonaCamara
        fields =  '__all__'
        #fields =  ('nombre_zona_camara','nro_personas',)
        #exclude = ('id_cliente',)

  
        