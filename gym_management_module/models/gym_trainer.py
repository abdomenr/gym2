from odoo import models, fields

class GymTrainer(models.Model):
    _name = 'gym.trainer'
    _description = 'Gym Trainer'

    name = fields.Char(required=True)
    specialty = fields.Char()
