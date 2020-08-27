# -*- encoding: utf-8 -*-
from django import forms
from camara_zona.models import CamaraZona
#from cliente.models import Cliente


class CamaraZonaForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial='')
    zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    clientes = forms.ChoiceField(label=u'Clientes')

    class Meta:
        model = CamaraZona
        fields = '__all__'
        exclude = ('id_camara_zona',)

    def __init__(self, *args, **kwargs):
        super(CamaraZonaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
        self.fields["clientes"].choices = [(str(c._id), c.razon_social) for c in
                                               Cliente.objects.all().filter(cliente_estado=True)]

class CamaraZonaFormWorking(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial='')
    zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
#    clientes = forms.ModelChoiceField(queryset=Cliente.objects.all().filter(cliente_estado=True))

    class Meta:
        model = CamaraZona
        fields = '__all__'
        exclude = ('id_camara_zona',)

    def __init__(self, *args, **kwargs):
        super(CamaraZonaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)



class CamaraZonaFormOLD(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial='')
    zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = CamaraZona
        fields = '__all__'
        exclude = ('id_camara_zona',)

    def __init__(self, *args, **kwargs):
        super(CamaraZonaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            self.fields["id_instalacion"].initial = {}


class CamaraZonaEditarForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    id_cliente = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial='')
    zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
#    clientes = forms.ChoiceField(label=u'Clientes')
    #Vehicle.objects.values('brand_name').distinct().order_by('brand_name')

    class Meta:
        model = CamaraZona
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CamaraZonaEditarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            arr_camara_zona = instance.id_camara_zona.split('_')
            if len(arr_camara_zona)>1:
                self.fields["camara_serial"].initial = str(arr_camara_zona[0]).upper()
                self.fields["zona_numero"].initial = arr_camara_zona[1]

        self.fields["id_cliente"].initial = str(instance.id_instalacion.id_cliente._id)
        self.fields["clientes"].choices = [(str(c._id), c.razon_social) for c in Cliente.objects.all().filter(cliente_estado=True)]