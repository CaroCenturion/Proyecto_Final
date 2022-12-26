from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Posteo, Comentar_post
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


@login_required
def Lista_Posteos(request):
    contexto = {}
    n = Posteo.objects.all()
    contexto['posteos'] = n

    
    return render(request, 'post\lista.html', contexto)
    
@login_required
def Detalle_Posteos(request, pk):
    contexto = {}

    n = Posteo.objects.get(pk = pk)
    contexto['posteo'] = n

    c = Comentar_post.objects.filter(posteos = n)
    contexto['comentarios'] = c

    return render(request, 'post\detalle.html', contexto)

@login_required
def Agregar_Comentario(request, pk):
    texto_comentario = request.POST.get('coment')
    posteos = Posteo.objects.get(pk = pk)
    c = Comentar_post.objects.create(post = pk, texto = texto_comentario, usuario = request.user)

    return HttpResponseRedirect(reverse_lazy('post:detalle', kwargs={'pk': pk})),
