# -*- encoding: utf-8 -*-
from django import forms
from camara_zona.models import CamaraZona
#from cliente.models import Cliente
from instalacion.models import Instalacion
from monitor.models import Monitor


class MonitorForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    #camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    #zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    clientes = forms.ChoiceField(label=u'Clientes')

    class Meta:
        model = Monitor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MonitorForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)

        self.fields["clientes"].choices = [(str(c._id), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]


class MonitorEditarForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    id_cliente = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    id_instalacion_s = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    #camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    #zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    clientes = forms.ChoiceField(label=u'Clientes')
    instalaciones = forms.ChoiceField(label=u'Instalaciones')
    camaras_zonas = forms.ChoiceField(label=u'Camara Zonas')

    class Meta:
        model = Monitor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MonitorEditarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)

        self.fields["id_cliente"].initial = str(instance.id_instalacion.id_cliente._id)
        self.fields["clientes"].choices = [(str(c._id), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]
        self.fields["instalaciones"].choices = [(str(c._id), c.nombre_comercial) for c in Instalacion.objects.all().filter(id_cliente=instance.id_instalacion.id_cliente._id, instalacion_estado=True)]
        self.fields["camaras_zonas"].choices = [(str(c._id), c.id_camara_zona) for c in CamaraZona.objects.all().filter(id_instalacion=instance.id_instalacion._id, camara_zona_estado=True)]


class MonitorShowForm(forms.ModelForm):
    personas = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = Monitor
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MonitorShowForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields["personas"].initial = "10"