# -*- encoding: utf-8 -*-
from django import forms
from aforoInfo.models import AforoInfo


class AforoInfoForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = AforoInfo
        fields = '__all__'
        # exclude = ('id_cliente',)

    def __init__(self, *args, **kwargs):
        super(AforoInfoForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)


