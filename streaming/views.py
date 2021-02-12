from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test,permission_required
from streaming.forms import StreamingForm
from django.utils.translation import activate


@login_required(login_url="/login/")
def streaming(request):
    activate('es')
    
    form = StreamingForm()
    
    return render(request, 'streaming/agregar.html', {'form': form})
