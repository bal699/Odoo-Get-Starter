# -*- coding: utf-8 -*-

from odoo import api, models, fields, tools, _


class SaleModel(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'gonzaga.sale'
    _description = 'Venda'

    # ----------------------------------------------------
    # Fields
    # ----------------------------------------------------

    name = fields.Char(
        string='Venda',
        related='partner_id.name'
    )

    sale_date = fields.Datetime(
        string='Data da Venda'
    )

    payment_condition = fields.Char(
        string='Condições de Pagamento',
        size=100,
        default='A VISTA'
    )

    partner_id = fields.Many2one(
        string='Cliente',
        comodel_name='res.partner'
    )

    sale_items = fields.One2many(
        string='Items',
        comodel_name='gonzaga.sale.item',
        inverse_name='sale_id'
    )


class SaleModelItem(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'gonzaga.sale.item'
    _description = 'Itens da Venda'

    # ----------------------------------------------------
    # Fields
    # ----------------------------------------------------

    sale_id = fields.Many2one(
        string='Venda',
        comodel_name='gonzaga.sale'
    )

    product_code = fields.Char(
        string='Codigo',
        size=10
    )

    description = fields.Char(
        string='Descrição',
        size=100
    )

    price = fields.Float(
        string='Valor'
    )
