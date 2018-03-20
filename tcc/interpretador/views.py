from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	resultado=[]
	texto=request.POST.get("handle", None)
	if(texto!=None):
		frases=texto.split("\n")
		for i in range(len(frases)):
			resultado.append(frases[i].split())
	else:
		texto=""
	context={'result1': texto,'result2':resultado}
	return render(request,'interpretador/index.html',context)