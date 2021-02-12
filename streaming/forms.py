# -*- encoding: utf-8 -*-
from django import forms
from streaming.models import Streaming 



class StreamingForm(forms.ModelForm):
    
    
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    
    
    class Meta:
        model = Streaming
        fields =  '__all__'


    def __init__(self, *args, **kwargs):
        super(StreamingForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            
                
         

        

  
                
         
