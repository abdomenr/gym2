from odoo import models, fields

class GymMember(models.Model):
    _name = 'gym.member'
    _description = 'Gym Member'

    name = fields.Char(required=True)
    membership_start_date = fields.Date(string="Membership Start Date")
    membership_end_date = fields.Date(string="Membership End Date")
    membership_fee = fields.Float(string="Membership Fee")
