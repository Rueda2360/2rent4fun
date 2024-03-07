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

    devuelto = fields.Boolean('Devuelto', default=False)

    def devolver_vehiculo(self):
        self.devuelto = True

    @api.constrains('fechaInicio')
    def funcionFechaPrestamo(self):
        for registro in self:
            if registro.fechaInicio and registro.fechaInicio > fields.Date.today():
                raise ValidationError('La fecha de alquiler no puede ser posterior al día de hoy.')

    @api.constrains('fechaDevolucion')
    def funcionFechaDevolucion(self):
        for registro in self:
            yesterday = fields.Date.today() - timedelta(days=1)
            if registro.fechaDevolucion and registro.fechaDevolucion < yesterday:
                raise ValidationError('La fecha prevista de vuelta no puede ser anterior al día de ayer.')
