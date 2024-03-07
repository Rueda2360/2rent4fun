# -*- coding: utf-8 -*-
{
    'name': "Renting",  # Titulo del módulo
    'summary': "Módulo realizado por aruedia202, SGE 23-24",  # Resumen de la funcionaliadad
    'description': """
    Gestion de alquiler de vehiculos
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Alejandro Rueda Díaz",
    'category': 'Extra Tools',
    'license': 'LGPL-3', 
    'version': '0.1',
    'depends': ['base'],

    'data': [

        'security/ir.model.access.csv',
        'views/flota_cliente.xml',
        'views/flota_vehiculo.xml',
        'views/flota_alquiler.xml'
        

        
        
    ],

}
