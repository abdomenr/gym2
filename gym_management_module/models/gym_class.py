from odoo import models, fields

class GymClass(models.Model):
    _name = 'gym.class'
    _description = 'Gym Class'

    name = fields.Char(required=True)
    trainer_id = fields.Many2one('gym.trainer', string='Trainer')
    schedule = fields.Datetime()
    max_capacity = fields.Integer()
    attendees = fields.Many2many('gym.member', string='Attendees')
