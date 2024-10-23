from django import forms

from apps.venta.models import Venta, Item


class NuevaVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['tipo_cliente', 'cliente_mayorista', 'tipo_venta', 'forma_pago', 'observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'class': 'form-control input-sm', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values(): #esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'



class NuevoItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['producto', 'cantidad']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in self.fields.values():  # esto es para cuestión de estilos
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'