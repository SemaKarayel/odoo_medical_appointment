from odoo import models, fields, api

class Patient(models.Model):
    _name = 'medical.patient'
    _description = 'Patient'

    # fields
    patient_id = fields.Char('Patient ID', required=True)
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    full_name = fields.Char(string='Full Name', compute='_compute_full_name', store=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', readonly=True)
    address = fields.Text('Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    national_id_no = fields.Char(string='National ID No')


    # unique national ID no constraint
    _sql_constraints = [
        ('national_id_no_unique', 'unique(national_id_no)', 'National ID number must be unique.')
    ]



    # Auto-generated patient id using ir.sequence
    # FILL HERE


    # compute full name
    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name} {rec.last_name}"


    # compute age
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - rec.date_of_birth.year - (
                    (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day)
                )
            else:
                rec.age = 0


    # Auto calculate age when user enter date of birth using onchange decorator
    @api.onchange('date_of_birth')
    def _onchange_date_of_birth(self):
        from datetime import date
        if self.date_of_birth:
            today = date.today()
            self.age = today.year - self.date_of_birth.year - (
                ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            )
        else:
            self.age = 0