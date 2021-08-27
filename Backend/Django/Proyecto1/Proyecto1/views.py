from django.http import HttpResponse
import datetime
def saludo(request):
    saludo="<html><body><h1>hola</h1></body></html>"
    return HttpResponse(saludo)
def despedida(request):
    return HttpResponse("Adios")
def damehora(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" %fecha_actual
    return HttpResponse(documento)