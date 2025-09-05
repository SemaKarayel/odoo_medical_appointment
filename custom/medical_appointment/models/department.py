from odoo import models, fields, api

class Department(models.Model):
    _name = 'medical.department'
    _description = 'Department'
    _rec_name = 'Code'

    # fields
    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)


    # code constraint
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Code must be unique.')
    ]

