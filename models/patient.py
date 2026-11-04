from odoo import models, fields,api
from datetime import date


class Patients(models.Model):
    _inherit = 'res.partner'

    is_patient = fields.Boolean(string="Is Patient")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age", compute="get_age")
    app_count = fields.Integer(string="count", compute="get_app_count")
    appointment_ids = fields.One2many(
        'the.appointments',
        'patient_id',
        string='Appointments'
    )

    @api.depends('birthdate')
    def get_age(self):
        today = date.today()

        for patient in self:
            if patient.birthdate:
                birthdate = patient.birthdate

                patient.age = (
                        today.year
                        - birthdate.year
                        - (
                                (today.month, today.day)
                                < (birthdate.month, birthdate.day)
                        )
                )
            else:
                patient.age = 0



    def get_appointment(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'the.appointments',
            'view_mode': 'list,form',
            'context': {
                'default_patient_id': self.id,
            },
        }

    @api.depends('appointment_ids')
    def get_app_count(self):
        for patient in self:
            patient.app_count = self.env['the.appointments'].search_count([
                ('patient_id', '=', patient.id)
            ])
