from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_supervisor = fields.Boolean(
        string='Is Supervisor'
    )