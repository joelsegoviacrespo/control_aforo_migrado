# -*- encoding: utf-8 -*-
from django import forms
from valores.models import Valores 
from cliente.models import Cliente
from instalacion.models import Instalacion


class ValoresForm(forms.ModelForm):
    
    PERCENT = 'PCT'
    NUMBER = 'NMB'

    FORMAT = (
        (PERCENT, 'Porcentaje'),
        (NUMBER, 'Número'),
    )

    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    cliente_nif = forms.ChoiceField()
    mostrar_valor = forms.ChoiceField(choices=FORMAT)
    
    class Meta:
        model = Valores
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super(ValoresForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        
         

class ValoresEditarForm(forms.ModelForm):
    PERCENT = 'PCT'
    NUMBER = 'NMB'

    FORMAT = (
        (PERCENT, 'Porcentaje'),
        (NUMBER, 'Número'),
    )

    
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    cliente_nif = forms.ChoiceField()
    id_cliente_nif = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    instalacion_n = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    instalacion_nombre = forms.ChoiceField()
    id_mostrar_valor = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    mostrar_valor = forms.ChoiceField(choices=FORMAT)
    
    class Meta:
        model = Valores
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super(ValoresEditarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
        
        #print("instance.cliente.nif")
        #print(instance.cliente)
        self.fields["id_cliente_nif"].initial = str(instance.instalacion.nif_cliente)
        self.fields["instalacion_n"].initial = str(instance.instalacion.nombre)
        self.fields["id_mostrar_valor"].initial = str(instance.mostrar_valor)    
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        
        instalacion_choices = [(instalacion.nombre_comercial, instalacion.nombre_comercial)                   
                                for instalacion in Instalacion.objects.all().filter(cliente={'nif': instance.instalacion.nif_cliente}, instalacion_estado=True)]
        
        self.fields["instalacion_nombre"] = forms.ChoiceField(choices=instalacion_choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        

  
                
         

