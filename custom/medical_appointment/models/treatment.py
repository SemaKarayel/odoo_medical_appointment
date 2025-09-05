from odoo import models, fields

class Treatment(models.Model):
    _name = 'medical.treatment'
    _description = 'Treatment'


    # fields
    name = fields.Char(string='Name', required=True)
    is_done = fields.Boolean(default=False)
