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

        #Aqui distintas vistas de equipo (vistas diferentes, mismo modelo)
        'views/liga_equipo.xml',
        'views/liga_equipo_clasificacion.xml',
        #Vista a un informe
        'report/liga_equipo_clasificacion_report.xml',
        #Aqui vista sobre los partidos
        'views/liga_partido.xml',
        #Añadimos un Wizard para introducir equipos
        'wizard/liga_equipo_wizard.xml',
        'wizard/liga_partido_wizard.xml'
        
        
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
