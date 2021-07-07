from django import forms 
from django.forms import ModelForm, widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Proveedor,Pais


class proveedorForm(ModelForm): 

    class Meta: 
        model = Proveedor 
        fields = ['idproveedor','foto','nombre_completo','telefono','direccion','email','contrasena','monedapago','pais']

        labels={
            'idproveedor': 'Digite Id',
            'foto': 'escoja producto', 
            'nombre': 'Digite Nombre del proveedor', 
            'telefono': 'Digite el telefono del proveedor',
            'direccion': 'Digite la su direccion',
            'email': 'Digite su email',
            'contrasena': 'Digite su contraseña',
            'monedapago': 'Indique medio de pago',
            'pais': 'seleccione id de su pais'
        }

        widgets={

            'idproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Id Proveedor', 
                    'id': 'idproveedor'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'from-control',
                    'placeholder': 'foto', 
                    'id': 'foto'
                }
            ),
            'nombre_completo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre Completo', 
                    'id': 'nombre_completo'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Telefono', 
                    'id': 'telefono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Dirección', 
                    'id': 'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Email', 
                    'id': 'email'
                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Contraseña', 
                    'id': 'contrasena'
                }
            ),
            'monedapago': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Moneda de pago', 
                    'id': 'monedapago'
                }
            ),
            'pais': forms.Select(    
                attrs={
                    'class': 'form-control', 
                    'id':'pais'
                }
            )  
        }