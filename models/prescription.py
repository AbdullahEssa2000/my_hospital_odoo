from odoo import models, fields, api, _


class Prescription(models.Model):
    _name = "the.prescription"
    _description = "Medical Prescription"

    name = fields.Char(
        string='Prescription ID',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New')
    )

    notes = fields.Text(
        string='Notes'
    )

    appointment_id = fields.Many2one(
        'the.appointments',
        string='Appointment',
        required=True,
        ondelete='cascade'
    )

    appointment_date = fields.Datetime(
        string='Appointment Date',
        related='appointment_id.app_date',
        store=True,
        readonly=True
    )

    patient_id = fields.Many2one(
        'res.partner',
        string='Patient',
        related='appointment_id.patient_id',
        store=True,
        readonly=True
    )

    doctor_id = fields.Many2one(
        'hr.employee',
        string='Doctor',
        related='appointment_id.doctor_id',
        store=True,
        readonly=True
    )

    line_ids = fields.One2many(
        'the.prescription.line',
        'prescription_id',
        string='Medicines'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = (
                    self.env['ir.sequence'].next_by_code(
                        'the.prescription.sequence'
                    ) or _('New')
                )

        return super().create(vals_list)