from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_medicine = fields.Boolean(
    string="Is Medicine")

    effective_material = fields.Char(
    string="Effective Material")