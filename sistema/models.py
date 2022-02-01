from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

CONDICION_CHOICE = [
	(0, 'CONTADO'),
	(1, 'CREDITO')
]

IVA_CHOICE =[
	(0, 'Exentas'),
	(5,	'IVA 5'),
	(10, 'IVA 10')
]

def path_and_rename(instance, filename):
	path = 'photos/profile'
	ext = filename.split('.')[-1]

	# set filename as random string
	filename = '{}.{}'.format(uuid4().hex, ext)

	# return the whole path to the file
	return os.path.join(path, filename)

class AperturaCaja(models.Model):
	class Meta:
		verbose_name = 'Apertura de caja'
		verbose_name_plural = 'Apertura de caja'
		ordering = ['-fecha']

	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)
	monto_apertura = models.IntegerField(default=0)
	monto_cierre = models.IntegerField(default=0)

	efectivo = models.IntegerField(default=0)
	tarjeta_debito = models.IntegerField(default=0)
	tarjeta_credito = models.IntegerField(default=0)

	vale_cobrado = models.IntegerField(default=0)
	vale_cobrar = models.IntegerField(default=0)

	monto_500 = models.IntegerField(default=0)
	monto_1000 = models.IntegerField(default=0)
	monto_2000 = models.IntegerField(default=0)
	monto_5000 = models.IntegerField(default=0)
	monto_10000 = models.IntegerField(default=0)
	monto_20000 = models.IntegerField(default=0)
	monto_50000 = models.IntegerField(default=0)
	monto_100000 = models.IntegerField(default=0)
	transferencia = models.IntegerField(default=0)

	def __str__(self):
		return 'apertura de caja' + self.fecha.strftime('%d/%m/%Y')

class Cliente(models.Model):
	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
		ordering = ['nombre']

	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	telefono = models.CharField(max_length=50, null=True, blank=True)
	celular = models.CharField(max_length=50, null=True, blank=True)
	direccion = models.TextField(null=True, blank=True)
	documento = models.CharField(verbose_name='RUC/CI', max_length=100)

	def __str__(self):
		return self.nombre + ' ' + self.apellido

class TipoArticulo(models.Model):
	class Meta:
		verbose_name = 'Tipo de artículo'
		verbose_name_plural = 'Tipos de artículo'

	descripcion = models.CharField(max_length=100)

	def __str__(self):
		return self.descripcion

class UnidadMedida(models.Model):
	class Meta:
		verbose_name = 'Unidad de medida'
		verbose_name_plural = 'Unidades de medida'
		ordering = ['descripcion']

	descripcion = models.CharField(max_length=100)
	abreviatura = models.CharField(max_length=10)

	def __str__(self):
		return self.abreviatura

class Articulo(models.Model):
	class Meta:
		verbose_name = 'Artículo'
		verbose_name_plural = 'Artículos'
		ordering = ['descripcion']

	descripcion = models.TextField()
	stock = models.IntegerField(default=0)
	precio = models.IntegerField()
	codigo_barra = models.CharField(max_length=100)
	codigo_manual = models.CharField(max_length=100)
	precio_venta = models.IntegerField()
	observacion = models.TextField()
	iva = models.PositiveSmallIntegerField(choices=IVA_CHOICE)
	usa_stock = models.BooleanField(default=False)
	tipo_articulo = models.ForeignKey(TipoArticulo, on_delete=models.RESTRICT)
	foto = models.ImageField(
		verbose_name = 'foto',
		upload_to=path_and_rename, 
		max_length=255, 
		default='default.jpg',
		null=True, 
		blank=True
	)
	unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.RESTRICT)


	def __str__(self):
		return self.descripcion

class Guarnicion(models.Model):
	class Meta:
		verbose_name = 'Guarnicion'
		verbose_name_plural = 'Guarnicion'
		ordering = ['descripcion']


	descripcion = models.CharField(max_length=100)
	costo_extra = models.IntegerField()

	def __str__(self):
		return self.descripcion

class Tyra(models.Model):
	class Meta:
		verbose_name = 'Tyra'
		verbose_name_plural = 'Tyra'
		ordering = ['descripcion']

	descripcion = models.CharField(max_length=100)
	costo_extra = models.IntegerField()

	def __str__(self):
		return self.descripcion

class ItemEnsalada(models.Model):
	class Meta:
		verbose_name = 'Item ensalada'
		verbose_name_plural = 'Item ensalada'
		ordering = ['descripcion']

	descripcion = models.CharField(max_length=100)
	costo_extra = models.IntegerField()

	def __str__(self):
		return self.descripcion


class TipoVenta(models.Model):
	class Meta:
		verbose_name = 'Tipo de venta'
		verbose_name_plural = 'Tipos de venta'
		ordering = ['descripcion']

	descripcion = models.CharField(max_length=100)

	def __str__(self):
		return self.descripcion


class Proveedor(models.Model):
	class Meta:
		verbose_name = 'Proveedor'
		verbose_name_plural = 'Proveedores'
		ordering = ['razon_social']

	ruc = models.CharField(max_length=100)
	razon_social = models.CharField(max_length=500)
	telefono = models.CharField(max_length=50, null=True, blank=True)
	direccion = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.razon_social


class Gasto(models.Model):
	class Meta:
		verbose_name = 'Otro gasto'
		verbose_name_plural = 'Otros Gastos'
		ordering = ['-fecha']

	detalle = models.TextField()
	monto = models.IntegerField()
	fecha = models.DateField()

	def __str__(self):
		return self.detalle


class PagoCheque(models.Model):
	class Meta:
		verbose_name = 'Pago cheque'
		verbose_name_plural = 'Pago cheque'
		ordering = ['-fecha']

	proveedor = models.ForeignKey(Proveedor, on_delete=models.RESTRICT)
	fecha = models.DateField()

	def __str__(self):
		return self.fecha.strftime('%d/%m/%Y')

class PagoChequeDetalle(models.Model):
	class Meta:
		verbose_name = 'Pago cheque detalle'
		verbose_name_plural = 'Pago cheque detalle'

	pago_cheque = models.ForeignKey(PagoCheque, on_delete=models.CASCADE)
	codigo_cheque = models.CharField(max_length=100)
	monto = models.IntegerField(default=0)

	def __str__(self):
		return self.codigo_cheque


class Compra(models.Model):
	class Meta:
		verbose_name = 'Compra'
		verbose_name_plural = 'Compras'
		ordering = ['-fecha']

	proveedor = models.ForeignKey(Proveedor, on_delete=models.RESTRICT)
	numero_factura = models.CharField(max_length=100)
	condicion = models.PositiveSmallIntegerField(choices=CONDICION_CHOICE, default=0)
	fecha = models.DateField()
	total = models.IntegerField()
	usuario = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, editable=False)


class PagoProveedor(models.Model):
	class Meta:
		verbose_name = 'Pago a proveedor'
		verbose_name_plural = 'Pagos a proveedores'
		ordering = ['-fecha']

	compra = models.ForeignKey(Compra, on_delete=models.RESTRICT)
	fecha = models.DateField()