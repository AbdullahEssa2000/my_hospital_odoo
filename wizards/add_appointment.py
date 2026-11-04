from odoo import fields, models, _


class AddAppointmentWizard(models.TransientModel):
    _name = 'add.appointment'
    _description = 'Add Appointment Wizard'

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

    notes = fields.Text(
        string='Notes'
    )

    app_date = fields.Datetime(
        string='Date Time',
        required=True
    )

    doctor_id = fields.Many2one(
        'hr.employee',
        string='Doctor',
        required=True,
        domain="[('is_doctor', '=', True)]"
    )

    def confirm_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'notes': self.notes,
            'app_date': self.app_date,
            'doctor_id': self.doctor_id.id,
        }

        self.env['the.appointments'].create(vals)