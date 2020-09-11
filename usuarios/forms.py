# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cliente.models import Cliente
from usuarios.models import User#, UsuarioEmbebido


class UsuariosForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    cliente_nif = forms.ChoiceField()

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UsuariosForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]

class UsuariosEditarForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    username = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    email = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    first_name = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    last_name = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    id_cliente_nif = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UsuariosEditarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
        
        #print("instance.cliente.nif")
        #print(instance.cliente)
        self.fields["id_cliente_nif"].initial = str(instance.cliente.nif_cliente)
        choices = [(cliente.nif, cliente.razon_social)                   
                   for cliente in  Cliente.objects.all()]
                   #for cliente in  Cliente.objects.filter(cliente_estado=True)[0]]
        
        self.fields['cliente_nif'] = forms.ChoiceField(choices=choices,required=False)
        
        usuarios_choices = [(usuarios.nombre_comercial, usuarios.nombre_comercial)                   
                                for usuarios in Usuario.objects.all().filter(cliente={'nif': instance.usuarios.nif_cliente}, usuarios_estado=True)]
        
        self.fields["usuarios_nombre"] = forms.ChoiceField(choices=usuarios_choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]

'''class UsuarioEmbebidoForm(forms.ModelForm):
    class Meta:
        model = UsuarioEmbebido
        fields =  ('nif_cliente','nombre',)  '''  
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
