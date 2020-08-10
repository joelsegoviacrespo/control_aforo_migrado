# -*- encoding: utf-8 -*-
from django import forms
from instalacion.models import Instalacion


class InstalacionForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = Instalacion
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super(InstalacionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)

