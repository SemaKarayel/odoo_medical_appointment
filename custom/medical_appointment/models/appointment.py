from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'medical.appointment'
    _description = 'Appointment'


    # fields
    appointment_date_time = fields.Datetime()
    code = fields.Char(string='Code', required=True)
    doctor = fields.Many2many('medical.doctor', string='Doctor')
    patient = fields.Many2one('medical.patient', string='Patient')
    stage = fields.Selection([
        ('draft', 'Draft'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ])
    treatment = fields.One2many('medical.treatment', 'appointment')


    # constraint
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Code must be unique.')
    ]


    # auto-generate code using ir.sequence
    # FILL HERE