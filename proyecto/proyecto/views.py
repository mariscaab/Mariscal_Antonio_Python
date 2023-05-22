from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):
    
    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name = "index.html"

    def post(self,request):
        return render(request)
    
    def get(self,request):
        datos = { "nombres": "Antonio De Jesus", 
                 "Primer_apellido": "Mariscal", 
                 "Segundo Apellido": "Bernal",
                 "fecha_nacimiento": "21 de abril de 1996",
                 "celular":"6672205867",
                 "correo":"antonio@hotmail.com",
                 "domicilio":"Prolonagacion Acueduto",
                 "genero":"masculino",
                 "objetivo":"mejorar cada dia",
                 "salario_esperado":"$5,000"}

        skills = ["SQL","UNIX","INGLES","SAP","Paquetes de Microsoft"]

        trabajos = {"lugar_trabajo":"AMDOCS",
                "año_inicio":"2022",
                "año_fin":"currently",
                "puesto":"Software Support Engineer",
                "lugar_trabajo1":"TATA",
                "año_inicio1":"2019",
                "año_fin1":"2022",
                "puesto1":"Support Executive" }

    

        return render (request, self.template_name,datos,skills,trabajos)