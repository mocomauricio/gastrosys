from django.contrib import admin
from django.contrib.admin.decorators import register
from django.utils.html import mark_safe 
from .models import *

# Register your models here.
@register(AperturaCaja)
class AperturaCajaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'hora', 'monto_apertura', 'monto_cierre']
    search_fields = ['fecha']
    list_per_page = 50


@register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'documento', 'telefono', 'celular']
    search_fields = ['nombre', 'apellido', 'documento']
    list_per_page = 50

@register(TipoArticulo)
class TipoArticuloAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ['descripcion']
    list_per_page = 50

@register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'abreviatura']
    search_fields = ['descripcion', 'abreviatura']
    list_per_page = 50


@register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['foto', 'descripcion', 'precio', 'codigo_barra', 'codigo_manual']
    search_fields = ['descripcion', 'codigo_barra', 'codigo_manual']
    list_filter = ['usa_stock', 'tipo_articulo']
    autocomplete_fields = ['tipo_articulo', 'unidad_medida']
    list_per_page = 50

@register(Guarnicion)
class GuarnicionAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'costo_extra']
    search_fields = ['descripcion']
    list_per_page = 50

@register(Tyra)
class TyraAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'costo_extra']
    search_fields = ['descripcion']
    list_per_page = 50

@register(ItemEnsalada)
class ItemEnsaladaAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'costo_extra']
    search_fields = ['descripcion']
    list_per_page = 50

@register(TipoVenta)
class TipoVentaAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ['descripcion']
    list_per_page = 50

@register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['ruc', 'razon_social', 'telefono', 'direccion']
    search_fields = ['ruc', 'razon_social']
    list_per_page = 50

@register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ['detalle', 'monto', 'fecha']
    search_fields = ['detalle']
    list_filter = ['fecha']
    list_per_page = 50


class PagoChequeDetalleAdmin(admin.TabularInline):
    model = PagoChequeDetalle

@register(PagoCheque)
class PagoChequeAdmin(admin.ModelAdmin):
    list_display = ['proveedor', 'fecha']
    list_filter = ['fecha']
    inlines = [PagoChequeDetalleAdmin,]
    autocomplete_fields = ['proveedor']
    list_per_page = 50
   



@register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['proveedor', 'numero_factura', 'condicion', 'fecha', 'total', 'usuario']
    search_fields = ['numero_factura']
    list_filter = ['condicion', 'fecha']
    autocomplete_fields = ['proveedor']
    list_per_page = 50

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        super().save_model(request, obj, form, change)