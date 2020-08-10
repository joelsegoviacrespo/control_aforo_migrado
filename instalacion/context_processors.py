from cliente.models import Cliente

def side_menu_instalaciones(request):
    instalaciones = Cliente.objects.all().filter(cliente_estado=True)
    #Entry.objects.filter(blog__startswith={'name': 'Beatles'})
    #.values_list("id","nombre_comercial") #.order_by("nombre_comercial").distinct("nombre_comercial")
    return {'menu_instalaciones': instalaciones}