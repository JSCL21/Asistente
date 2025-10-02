from django.shortcuts import render

def lista_modulos(request):
    # Datos de ejemplo para los módulos
    modulos = [
        {'id': 1, 'titulo': 'Fundamentos Digitales', 'descripcion': 'Conceptos básicos...', 'orden': 1},
        {'id': 2, 'titulo': 'Comunicación Digital', 'descripcion': 'Herramientas de comunicación...', 'orden': 2},
        {'id': 3, 'titulo': 'Creación de Contenido', 'descripcion': 'Desarrollo de contenido...', 'orden': 3},
        {'id': 4, 'titulo': 'Seguridad Digital', 'descripcion': 'Protección y seguridad...', 'orden': 4},
        {'id': 5, 'titulo': 'Resolución de Problemas', 'descripcion': 'Solución de issues...', 'orden': 5},
    ]
    
    return render(request, 'modulos/lista_modulos.html', {'modulos': modulos})