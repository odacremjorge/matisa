# -*- COTIZACION ORDEN DE TRABAJO -*-

from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from apps.inicio.mixins import LoginRequiredMixin
from apps.empleado.models import Empleado
from .models import CotizacionOrdenDeTrabajo

class CotizacionOrdenDeTrabajoDetailView(LoginRequiredMixin, TemplateView):

	def get(self,request,*args,**kwargs):
		cotizacion = CotizacionOrdenDeTrabajo.objects.get(id=kwargs['pk'])
		context = { 'cotizacion':cotizacion }

		return render(request, 'cotizacion_orden_de_trabajo/detalle.html', context)

class CotizacionOrdenDeTrabajoListView(LoginRequiredMixin, TemplateView):

	def get(self,request,*args,**kwargs):
		empleado = Empleado.objects.get(id=request.user.empleado.id)
		cotizaciones = CotizacionOrdenDeTrabajo.objects.filter(
			orden_de_trabajo__empleado = empleado
			)

		context = {
			'cotizaciones':cotizaciones
		 }
		return render(request, 'cotizacion_orden_de_trabajo/list.html', context)
