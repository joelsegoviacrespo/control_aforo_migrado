# -*- encoding: utf-8 -*-
from django import forms
from objectsDetector.models import Objects 



class ObjectsForm(forms.ModelForm):
    
    
    #id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    #label=forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    
    
    class Meta:
        model = Objects
        fields =  '__all__'


    def __init__(self, *args, **kwargs):
        super(ObjectsForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
        
            
            
                
         

        

  
                
         
