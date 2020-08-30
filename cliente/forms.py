# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from cliente.models import Cliente,ClienteEmbebido


class ClienteForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    # usuarios = forms.ModelChoiceField(queryset=User.objects.all())
    # staff = User.objects.filter(is_staff=True)

    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ('numero_cliente',)

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)


class ClienteTodosForm(forms.ModelForm):
    clientes = forms.ChoiceField(widget=forms.Select, choices=Cliente.objects.all(), required=False,
                                 help_text="clientes")

    class Meta:
        model = Cliente
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     print('oooo')


class ClienteEmbebidoForm(forms.ModelForm):
    

    class Meta:
        model = ClienteEmbebido
        #fields =  '__all__'
        fields =  ('nif',)
        #exclude = ('id_cliente',)

  
        