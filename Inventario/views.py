from django.shortcuts import render
from datetime import date, datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from Pacientes.models import Inventario
import base64
from django.db.models import Sum
import json
# Create your views here.

def es_administrador(user):
    return user.groups.filter(name='Administrador').exists()

@login_required
@user_passes_test(es_administrador)
def index(request):
    return render(request,'index.html')

@login_required
@user_passes_test(es_administrador)
def ListarInventario(request):
    productos = Inventario.objects.all()
    total_productos = productos.count()
    total_stock = productos.aggregate(total_stock=Sum('cantidad'))['total_stock']

    # Obtener la cantidad de productos por categoría
    categorias = ['Higiene y Desinfección', 'Herramientas de Diagnóstico', 'Material de Oficina', 'Productos para terapias', 'Equipo de tratamiento']
    productos_por_categoria = [productos.filter(categoria=categoria).count() for categoria in categorias]

    # Convertir las listas a cadenas JSON
    categorias_json = json.dumps(categorias)
    productos_por_categoria_json = json.dumps(productos_por_categoria)

    return render(request, 'Vistas_Inventario/GestionInventario.html', {
        'productos': productos,
        'total_productos': total_productos,
        'total_stock': total_stock,
        'categorias': categorias_json,
        'productos_por_categoria': productos_por_categoria_json,
    })

@login_required
@user_passes_test(es_administrador)
def RegistrarProducto(request):
    
    nuevo_producto = Inventario()  # Inicializamos la variable fuera del bloque if
    
    if request.method == 'POST':
        nombre_suministro = request.POST['nombre_suministro']
        cantidad = request.POST['cantidad']
        costo_unitario = request.POST['costo_unitario']
        # fecha_vencimiento = request.POST['fecha_vencimiento']
        decripcion = request.POST['descripcion_suministro']
        imagen = request.FILES.get('imagen')
        categoria = request.POST['categoria']
        
        nuevo_producto.nombre_suministro = nombre_suministro
        nuevo_producto.cantidad = cantidad
        nuevo_producto.costo_unitario = costo_unitario
        # nuevo_producto.fecha_vencimiento = fecha_vencimiento
        nuevo_producto.descripcion = decripcion
        nuevo_producto.categoria = categoria
        
        if imagen:
            nuevo_producto.imagenprod = imagen.read()
        
        nuevo_producto.save()
        
        messages.success(request, "El Producto se ha registrado satisfactoriamente")
        return redirect('GestionInventario')
            
    return render(request,'Vistas_Inventario/registrarProducto.html',{
        'producto' : nuevo_producto,
    })

    

@login_required
@user_passes_test(es_administrador)
def DetallesProducto(request, id_suministro):
    producto = get_object_or_404(Inventario, pk=id_suministro)

    imagen_data_uri = None
    
    if producto.imagenprod:
        # Convertir los datos binarios de la imagen a una URL de datos URI
        imagen_base64 = base64.b64encode(producto.imagenprod).decode('utf-8')
        imagen_data_uri = f"data:image/jpeg;base64,{imagen_base64}"
    
    return render(request, 'Vistas_Inventario/DetallesProducto.html', {
        'producto': producto,
        'imagen_data_uri': imagen_data_uri,
    })
    
@login_required
@user_passes_test(es_administrador)
def EliminarProducto(request, id_suministro):
    producto = get_object_or_404(Inventario, id_suministro=id_suministro)

    if request.method == 'POST':
        #Deshabilitar la Consulta
        producto.delete()
        # Redirigir al usuario a la página de lista de consultas o cualquier otra página que desees mostrar después de eliminar la consulta
        messages.success(request, "El producto se ha eliminado satisfactoriamente")
        return redirect('GestionInventario')

    return render(request, 'Vistas_Inventario/EliminarProducto.html', {'producto': producto,})   

@login_required
@user_passes_test(es_administrador)
def EditarProducto(request, id_suministro):
    
    producto = get_object_or_404(Inventario, id_suministro=id_suministro)
    
    if request.method == 'POST':
        
        nombre_suministro = request.POST['nombre_suministro']
        cantidad = request.POST['cantidad']
        costo_unitario = request.POST['costo_unitario']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        imagen = request.FILES.get('imagen')
        descripcion = request.POST['descripcion_suministro']
        categoria = request.POST['categoria']
        
        producto.nombre_suministro = nombre_suministro
        producto.cantidad = cantidad
        producto.costo_unitario = costo_unitario
        producto.fecha_vencimiento = fecha_vencimiento
        producto.descripcion = descripcion
        producto.categoria = categoria
        
        if imagen:
            # Si se proporcionó una nueva imagen, reemplazar la anterior
            producto.imagenprod = imagen.read()
                
        producto.save()
        messages.success(request, "El Producto se ha editado satisfactoriamente")
        return redirect('DetallesProducto', id_suministro=id_suministro)
    
    imagen_base64 = producto.get_imagenprod_base64()
        
    return render(request,'Vistas_Inventario/EditarProducto.html', {
        'producto': producto,
        'imagen_base64': imagen_base64,
    })