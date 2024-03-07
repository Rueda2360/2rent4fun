# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields



class FlotaVehiculo(models.Model):

    #Nombre y descripcion del modelo
    _name = 'flota.vehiculo'

    _description = 'Vehiculo de la flota'

    #Parametros de ordenacion por defecto
    _order = 'marca'
    _rec_name = 'matricula'
    #ATRIBUTOS

    marca = fields.Char('Marca',required=True)
    matricula = fields.Char('Matricula',required=True)
    foto = fields.Image('Image',max_width=150,max_height=150)
    estado = fields.Char('Estado',required=True)
    
    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    


    


