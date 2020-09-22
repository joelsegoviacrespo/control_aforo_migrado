from django import forms
from camaras_historico.models import myCamaras

class Camaras_historicoForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = myCamaras
        fields = '__all__'
        # exclude = ('id_cliente',)

    def __init__(self, *args, **kwargs):
        super(Camaras_historicoForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)


  