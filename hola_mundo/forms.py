from django import forms

class TareasForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100)
    creado_el = forms.DateField()
    modificado_el = forms.DateField()


class BuscarTareasForm(forms.Form):
    criterio_tarea =forms.CharField(max_length=100)
    
class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()


class BuscarPersonasForm(forms.Form):
    criterio_nombre =forms.CharField(max_length=100)


class ComprasForm(forms.Form):
    articulo = forms.CharField(max_length=100)
    precio = forms.CharField(max_length=100)
    fecha_de_compra = forms.DateField()

class BuscarComprasForm(forms.Form):
    criterio_articulo =forms.CharField(max_length=100)
    