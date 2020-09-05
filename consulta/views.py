from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers

from .models import Consulta, Resultado
from .forms import ConsultaForm, ResultadoForm


@login_required
def home(request):
    return render(request, 'consulta/home.html')


@login_required
def listaConsultas(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    if search:
        #consultas = Consulta.objects.filter(data__icontains=search)
        consultas = Consulta.objects.filter(data__icontains=search, cliente=request.user)
    elif filter:
        #consultas = Consulta.objects.filter(done=filter)
        consultas = Consulta.objects.filter(done=filter, cliente=request.user)
    else:
        lista_consultas = Consulta.objects.all().order_by("data").filter(cliente=request.user)
        #lista_consultas = Consulta.objects.all().order_by("data")
        paginator = Paginator(lista_consultas, 3)
        pagina = request.GET.get('page')
        consultas = paginator.get_page(pagina)

    return render(request, 'consulta/lista.html', {'consultas':consultas})

@login_required
def consultaView(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    return render(request, 'consulta/consulta.html', {'consulta': consulta})

@login_required
def novaConsulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            #consulta = form.save()
            consulta = form.save(commit=False)
            consulta.cliente = request.user
            consulta.save()
            return redirect('/')
        else:
            return render(request, 'consulta/addConsulta.html', {'form': form})
    else:
        form = ConsultaForm()
        return render(request, 'consulta/addConsulta.html', {'form': form})

@login_required
def editaConsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    form = ConsultaForm(instance=consulta)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta )
        if form.is_valid():
            consulta.save()
            return redirect('/')
        else:
            return render(request, 'consulta/editaConsulta.html', {'form': form, 'consulta': consulta})
    else:
        return render(request, 'consulta/editaConsulta.html', {'form': form, 'consulta': consulta})

@login_required
def deletaConsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    consulta.delete()

    messages.info(request, 'Consulta deletada')
    return redirect('/')

    
def sendJson(request, id):
    data = [{'name': 'Peter', 'email': 'peter@example.org'}, {'name': 'Julia', 'email': 'julia@example.org'}]
    lista_consultas = Consulta.objects.all().order_by("data").filter(cliente=request.user)
    #selecionei alguns campos para poder mostrar que é possivel usar apenas alguns deles
    post_list = serializers.serialize('json', lista_consultas, fields=('medico','data', 'hora'))
    #resultado = post_list.replace("\\\"","")#"\","")
    return JsonResponse(post_list, safe=False)