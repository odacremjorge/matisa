# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from concesionario import settings
from django.conf.urls.static import static

urlpatterns = [

	url(r'^admin/', admin.site.urls),
    url(r'', include(('apps.inicio.url','inicio'),namespace='inicio')),
    url(r'', include(('apps.cuenta.url','cuenta'),namespace='cuenta')),
    url(r'', include(('apps.cotizacion.url','cotizacion'),namespace='cotizacion')),
    url(r'', include(('apps.cliente.url','cliente'),namespace='cliente')),
    url(r'', include(('apps.empleado.url','empleado'),namespace='empleado')),
    url(r'', include(('apps.repuesto.url','repuesto'),namespace='repuesto')),
    url(r'', include(('apps.sucursal.url','sucursal'),namespace='sucursal')),
    url(r'', include(('apps.vehiculo.url','vehiculo'),namespace='vehiculo')),
    url(r'', include(('apps.venta.url','venta'),namespace='venta')),
    url(r'', include(('apps.proveedor.url','proveedor'),namespace='proveedor')),
    url(r'', include(('apps.reporte.url','reporte'),namespace='reporte')),
    url(r'', include(('apps.orden_de_trabajo.url','orden_de_trabajo'),namespace='orden_de_trabajo')),
    url(r'', include(('apps.cotizacion_orden_de_trabajo.url','cotizacion_orden_de_trabajo'),namespace='cotizacion_orden_de_trabajo')),
	url(r'', include(('apps.factura_orden_de_trabajo.url','factura_orden_de_trabajo'),namespace='factura_orden_de_trabajo')),
    url(r'', include(('apps.movil.url','movil'),namespace='movil')),

    #url para acceder a la imagenes que estan en la carpeta media del proyecto
    #se deseas colocar imagenes en tu contenido HTML, este link es necesario para que se muestren las imagenes
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
