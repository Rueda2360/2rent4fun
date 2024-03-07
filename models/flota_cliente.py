# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields,api



class FlotaCLiente(models.Model):

    #Nombre y descripcion del modelo
    _name = 'flota.cliente'

    _description = 'Cliente de la empresa'

    #Parametros de ordenacion por defecto
    _order = 'nombre'
    _rec_name = 'nombreCompleto'

    #ATRIBUTOS

    

    
    nombre = fields.Char('Nombre')
    apellido = fields.Char('Apellido')

    nombreCompleto = fields.Char('Nombre Completo', compute='_compute_nombre_completo', store=True)

    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombreCompleto = f"{record.nombre} {record.apellido}"
    


