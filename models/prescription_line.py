from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PrescriptionLine(models.Model):
    _name = "the.prescription.line"
    _description = "Prescription Line"

    product_id = fields.Many2one(
        'product.product',
        string='Medicine',
        required=True,
        domain="[('product_tmpl_id.is_medicine', '=', True)]",
        ondelete='restrict'
    )

    notes = fields.Text(
        string='Notes'
    )

    prescription_id = fields.Many2one(
        'the.prescription',
        string='Prescription',
        required=True,
        ondelete='cascade'
    )

    quantity = fields.Float(
        string='Quantity',
        required=True,
        default=1.0
    )

    dosage = fields.Char(
        string='Dosage'
    )

    instructions = fields.Text(
        string='Instructions'
    )

    @api.constrains('product_id')
    def _check_product_is_medicine(self):
        for line in self:
            if (
                line.product_id
                and not line.product_id.product_tmpl_id.is_medicine
            ):
                raise ValidationError(
                    "The selected product must be marked as a medicine."
                )