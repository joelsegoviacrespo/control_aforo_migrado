# -*- encoding: utf-8 -*-
from django import forms
from fondos.models import Fondos,FondosEmbebido 
from cliente.models import Cliente
from instalacion.models import Instalacion


class FondosForm(forms.ModelForm):
    
    HORIZONTAL = 'HRZ'
    VERTICAL = 'VRT'

    ORIENTACION_CHOICES = (
        (HORIZONTAL, 'Horizontal'),
        (VERTICAL, 'Vertical'),
    )
    
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    numero_cliente = forms.CharField(widget=forms.HiddenInput, required=False, initial="")
    cliente_nif = forms.ChoiceField()
    orientacion = forms.ChoiceField(choices=ORIENTACION_CHOICES)    
    
    class Meta:
        model = Fondos
        fields =  '__all__'
        #exclude = ('nombre_archivo_verde','nombre_archivo_ambar','nombre_archivo_rojo','nombre_archivo_cerrado',)

    def __init__(self, *args, **kwargs):
        super(FondosForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        
         

class FondosEditarForm(forms.ModelForm):
    
    HORIZONTAL = 'HRZ'
    VERTICAL = 'VRT'

    ORIENTACION_CHOICES = (
        (HORIZONTAL, 'Horizontal'),
        (VERTICAL, 'Vertical'),
    )

    
    
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    cliente_nif = forms.ChoiceField()
    id_cliente_nif = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    instalacion_n = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    instalacion_nombre = forms.ChoiceField()
    id_orientacion = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    orientacion = forms.ChoiceField(choices=ORIENTACION_CHOICES)
    numero_cliente = forms.CharField(widget=forms.HiddenInput, required=False)

    
    class Meta:
        model = Fondos
        fields =  '__all__'
        #exclude = ('url_verde','url_ambar','url_rojo','url_cerrado','nombre_archivo_verde','nombre_archivo_ambar','nombre_archivo_rojo','nombre_archivo_cerrado',)

    def __init__(self, *args, **kwargs):
        super(FondosEditarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
        
        #print("instance.cliente.nif")
        #print(instance.cliente)
        self.fields["id_cliente_nif"].initial = str(instance.instalacion.nif_cliente)
        self.fields["instalacion_n"].initial = str(instance.instalacion.nombre)
        self.fields["id_orientacion"].initial = str(instance.orientacion)
        
        cliente = Cliente.objects.get(nif=instance.instalacion.nif_cliente, cliente_estado=True)
        self.fields["numero_cliente"].initial = cliente.numero_cliente 
                   
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        
        instalacion_choices = [(instalacion.nombre_comercial, instalacion.nombre_comercial)                   
                                for instalacion in Instalacion.objects.all().filter(cliente={'nif': instance.instalacion.nif_cliente}, instalacion_estado=True)]
        
        self.fields["instalacion_nombre"] = forms.ChoiceField(choices=instalacion_choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        
class FondosEmbebidoForm(forms.ModelForm):
    

    class Meta:
        model = FondosEmbebido        
        fields =  ('descripcion','orientacion','url_verde','url_ambar','url_rojo','url_cerrado','hora_apertura','hora_cierre')

  
                
         
