from django.shortcuts import render

# Create your views here.
def index(request):
    lista_articulos = [
        {
            "titulo":"Mover, copiar y renombrar directorios en Linux",
            "imagen":"https://app.ed.team/_next/image?url=https%3A%2F%2Fedteam-media.s3.amazonaws.com%2Fblogs%2Foriginal%2F511e1605-3a2a-46ba-a211-ff5d33d6028f.png&w=1920&q=75",
            "autor":"Alvaro Felipe Chávez",
        },
        {
            "titulo":"La historia de Ubuntu, la distribución más popular de Linux",
            "imagen":"https://app.ed.team/_next/image?url=https%3A%2F%2Fedteam-media.s3.amazonaws.com%2Fblogs%2Foriginal%2F02736ec5-de79-467a-a5c9-0b72927bc418.jpeg&w=1920&q=75",
            "autor":"Yimmerlys Lopez",
        },
        {
            "titulo":"¿Por qué en mi máquina funciona y en las demás no?",
            "imagen":"https://app.ed.team/_next/image?url=https%3A%2F%2Fedteam-media.s3.amazonaws.com%2Fblogs%2Foriginal%2Fc08a113f-937e-4159-9c5e-7e6ea03851ee.png&w=1920&q=75",
            "autor":"Alvaro Felipe Chávez",
        },
    ]
    
    context = {
        "articulos": lista_articulos
    }
    return render(request, 'index.html', context)