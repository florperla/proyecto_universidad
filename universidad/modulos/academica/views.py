from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def formulario_contacto(request):
    return render(request, "formulario_contacto.html")

def contactenos(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        mail_desde = settings.EMAIL_HOST_USER
        mail_para = ["florrchuperla@gmail.com"]
        send_mail(asunto, mensaje, mail_desde, mail_para, fail_silently=False)
        return render(request, "contacto_exitoso.html")
    return render(request, "formulario_contacto.html")