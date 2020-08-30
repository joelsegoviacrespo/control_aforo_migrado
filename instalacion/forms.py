# -*- encoding: utf-8 -*-
from django import forms
from instalacion.models import Instalacion
from cliente.models import Cliente


class InstalacionForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    cliente_nif = forms.ChoiceField()
    
    class Meta:
        model = Instalacion
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super(InstalacionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        
         

class InstalacionEditarForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    cliente_nif = forms.ChoiceField()
    id_cliente_nif = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    
    class Meta:
        model = Instalacion
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super(InstalacionEditarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
        
        #print("instance.cliente.nif")
        #print(instance.cliente)
        self.fields["id_cliente_nif"].initial = str(instance.cliente.nif)    
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        
         

