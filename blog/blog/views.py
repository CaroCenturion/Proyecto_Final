from django.shortcuts import render

#request 'es un diccionario que continuamente se va pasando entre el navegador y el servidor'

def Home(request):

	return render(request, 'home.html')

def registro(request):

    return render(request, 'registro.html')    

def blog(request):

	return render(request, 'blog.html')
