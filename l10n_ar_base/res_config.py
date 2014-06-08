# -*- coding: utf-8 -*-
##############################################################################
#
#    Sistemas ADHOC - ADHOC SA
#    https://launchpad.net/~sistemas-adhoc
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging

from openerp.osv import fields, osv

_logger = logging.getLogger(__name__)

class argentinian_base_configuration(osv.osv_memory):
    _name = 'argentinian.base.config.settings'
    _inherit = 'res.config.settings'

    _columns = {
        'module_l10n_ar_chart_generic': fields.boolean('Generic Argentinian Chart of Account',
            help = """Installs the l10n_ar_chart_generic module."""),
        'module_l10n_ar_bank': fields.boolean('Banks of Argentina',
            help = """Installs the l10n_ar_bank module that create banks of Argetina based on a webservice"""),
        'module_l10n_ar_base_vat': fields.boolean('Argentinian VAT validation',
            help = """Installs the l10n_ar_base_vat module that extends base_vat modules so that you can add argentinian VATs (usually called cuit/cuil)"""),
        'module_l10n_ar_invoice': fields.boolean('Argentinian invoicing and other documents Management',
            help = """Installs the l10n_ar_invoice module. It creates some clases to manage afip functionality, for example document class, journal class, document letters, vat categories, etc."""),          
        'module_l10n_ar_partner_title': fields.boolean('Partner reference and titles usually used in Argentina',
            help = """Installs the l10n_ar_partner_title module. """),
        'module_l10n_ar_states': fields.boolean('Argentinian States',
            help = """Installs the l10n_ar_states module. """), 
        'module_l10n_ar_vat_reports': fields.boolean('Argentinian Sale/Purchase Vat Reports',
            help = """Installs the l10n_ar_vat_reports module. """),                                                      
        'module_l10n_ar_aeroo_reports': fields.boolean('Aeroo Reports for Sales, Purchases, Pickings, Invoices based on aeroo reports with typical Argentinean format.',
            help = """Installs the l10n_ar_aeroo_reports module. """),
        'module_l10n_ar_hide_receipts': fields.boolean('Hide sale/purchase receipts menus.',
            help = """Installs the l10n_ar_hide_receipts module. """),        
        'module_account_accountant': fields.boolean('Manage Financial and Analytic Accounting.',
            help = """Installs the account_accountant module. """),                         
        # 'default_coding_method':fields.selection([('category','Based on the Category'), ('group','Based on Major / Sub Groups')], required=True, default_model='product.product'),
    }        
    
    _defaults = {
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: