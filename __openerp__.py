# -*- coding: utf-8 -*-
{
    'name': "sp_pos_search",

    'summary': """
        Amélioration de la recherche sur le pos""",

    'description': """
         Permet une recherche avec accents
    """,

    'author': "Supercoop",
    'website': "https://github.com/supercoopbdx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Supercoop',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/resources.xml',
        # 'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
