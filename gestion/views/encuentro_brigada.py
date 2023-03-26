from django.shortcuts import render
from backend.forms import InscripcionEncuentroForm

def home_encuentro (request):
    return render(request, 'app/encuentro_brigada/home.html')


def inscripcion_encuentro(request):
    data = {
        'form' : InscripcionEncuentroForm()
    }

    if request.method == 'POST':
        formulario = InscripcionEncuentroForm(data= request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Inscripción realizada con exito'
        else:
            data['form'] = formulario
    return render(request, 'app/encuentro_brigada/inscripcion.html', data)

