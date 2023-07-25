from django.shortcuts import render
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from Pacientes.models import Inventario
import base64
# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def ListarInventario(request):
    productos = Inventario.objects.all()
    
    return render(request,'Vistas_Inventario/GestionInventario.html',{
        'productos': productos,
    })

@login_required
def RegistrarProducto(request):
    
    if request.method == 'POST':
        nombre_suministro = request.POST['nombre_suministro']
        cantidad = request.POST['cantidad']
        costo_unitario = request.POST['costo_unitario']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        imagen = request.FILES.get('imagen')
        
        nuevo_producto = Inventario()
        nuevo_producto.nombre_suministro = nombre_suministro
        nuevo_producto.cantidad = cantidad
        nuevo_producto.costo_unitario = costo_unitario
        nuevo_producto.fecha_vencimiento = fecha_vencimiento
        
        if imagen:
            nuevo_producto.imagenprod = imagen.read()
        
        nuevo_producto.save()
        
        messages.success(request, "El Producto se ha registrado satisfactoriamente")
        return redirect('GestionInventario')
         
    return render(request,'Vistas_Inventario/registrarProducto.html')

@login_required
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
def EditarProducto(request, id_suministro):
    
    producto = get_object_or_404(Inventario, id_suministro=id_suministro)
    
    if request.method == 'POST':
        
        nombre_suministro = request.POST['nombre_suministro']
        cantidad = request.POST['cantidad']
        costo_unitario = request.POST['costo_unitario']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        imagen = request.FILES.get('imagen')
        
        producto.nombre_suministro = nombre_suministro
        producto.cantidad = cantidad
        producto.costo_unitario = costo_unitario
        producto.fecha_vencimiento = fecha_vencimiento
        
        if imagen:
            # Si se proporcionó una nueva imagen, reemplazar la anterior
            producto.imagenprod = imagen.read()
        
        # Guardar el nombre de la imagen actual en el atributo data del campo de entrada de imagen
        if producto.imagenprod:
            imagen_input = 'inputImagen'
            imagen_input_field = request.FILES.get('imagen')
            
            if imagen_input_field:
                imagen_current_name = imagen_input_field.name
                producto.imagenprod.name = imagen_current_name
                input_imagen_html = '<input type="file" class="custom-file-input" id="inputImagen" name="imagen" data-current-name="{}">'
                imagen_input = input_imagen_html.format(imagen_current_name)
                
        producto.save()
        messages.success(request, "El Producto se ha editado satisfactoriamente")
        return redirect('DetallesProducto', id_suministro=id_suministro)
    
    return render(request,'Vistas_Inventario/EditarProducto.html', {
        'producto': producto,
    })