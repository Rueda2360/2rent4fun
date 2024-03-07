# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from openerp.exceptions import ValidationError

class FlotaAlquiler(models.Model):
    _name = 'flota.alquiler'
    _description = 'Préstamo de cómic'

    matriculaCoche = fields.Many2one('flota.vehiculo', string='Matrícula del coche',required=True)
    nombreCliente = fields.Many2one('flota.cliente', string='Cliente', required=True)
    fechaInicio = fields.Date('Fecha de inicio', default=fields.Date.today(), required=True)
    fechaDevolucion = fields.Date('Fecha de devolución prevista', required=True)

    #disponible = fields.Boolean('Disponible', default=False)

    @api.constrains('matriculaCoche')
    def estadoVehiculo(self):
        for record in self:
            if record.matriculaCoche.estado != 'Disponible':
                raise ValidationError('El vehículo seleccionado no está disponible para alquilar.')
            
    @api.constrains('fechaInicio')
    def funcionFechaPrestamo(self):
        for registro in self:
            if registro.fechaInicio >= fields.Date.today():
                raise ValidationError('La fecha de alquiler no puede ser igual o posterior al día de hoy.')
