from odoo import models, fields, api, _


class TheAppointments(models.Model):
    _name = "the.appointments"
    _description = "Appointments"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _sql_constraints = [
        (
            'unique_doctor_appointment_date',
            'unique(doctor_id, app_date)',
            'This doctor already has an appointment at this date and time.',
        )
    ]

    name = fields.Char(
        string='Appointment Id',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New')
    )

    patient_id = fields.Many2one(
        'res.partner',
        string='Patient',
        required=True,
        domain="[('is_patient', '=', True)]"
    )

    patient_age = fields.Integer(
        string='Age',
        related='patient_id.age'
    )

    app_date = fields.Datetime(
        string='Date Time',
        required=True
    )

    notes = fields.Text(
        string='Notes'
    )

    doctor_id = fields.Many2one(
        'hr.employee',
        string='Doctor',
        required=True,
        domain="[('is_doctor', '=', True)]"
    )

    doctor_notes = fields.Text(
        string='Doctor Notes'
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirm', 'Confirmed'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
        string='Status',
        readonly=True,
        default='draft'
    )

    prescription_ids = fields.One2many(
        'the.prescription',
        'appointment_id',
        string='Prescriptions'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = (
                    self.env['ir.sequence'].next_by_code(
                        'the.appointments.sequence'
                    ) or _('New')
                )

        return super().create(vals_list)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        for record in self:
            if self.patient_id:
                record.notes=f"Patient : {self.patient_id.name}"

    def action_confirm(self):
        for appointment in self:
            appointment.state = 'confirm'

    def action_done(self):
        for appointment in self:
            appointment.state = 'done'

    def action_cancel(self):
        for appointment in self:
            appointment.state = 'cancel'