# -*- EMPLEADO -*-

from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
from apps.inicio.mixins import LoginRequiredMixin
from .models import Empleado
from apps.sucursal.models import Sucursal



class EmpleadoListView(LoginRequiredMixin, TemplateView):

	def get(self,request,*args,**kwargs):
		sucursal_id = kwargs['spk']
		empleados = Empleado.objects.filter(sucursal_id=sucursal_id).exclude(user_id=request.user.id)
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context = {
		'sucursal':sucursal,
		'empleados':empleados}
		return render(request, 'empleado/empleado_list.html', context)
