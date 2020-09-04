# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import Usuarios 
from cliente.models import Cliente
from instalacion.models import Instalacion, InstalacionEmbebido


class UsuariosForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    cliente_nif = forms.ChoiceField()

    class Meta:
        model = Usuarios
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
    cliente_nif = forms.ChoiceField()
    id_cliente_nif = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    
    class Meta:
        model = Usuarios
        fields =  '__all__'

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
        
        instalacion_choices = [(instalacion.nombre_comercial, instalacion.nombre_comercial)                   
                                for instalacion in Instalacion.objects.all().filter(cliente={'nif': instance.instalacion.nif_cliente}, instalacion_estado=True)]
        
        self.fields["instalacion_nombre"] = forms.ChoiceField(choices=instalacion_choices,required=False)
        #self.fields["clientes"].choices = [(str(c.nif), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        

class SignUpForm(UserCreationForm):
    is_active = forms.BooleanField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Activo",                
                "class": "form-control"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Nombre",                
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Apellido",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))
   

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
                
         

