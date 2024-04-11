from odoo import models, fields

class GymEquipment(models.Model):
    _name = 'gym.equipment'
    _description = 'Gym Equipment'

    name = fields.Char(required=True)
    type = fields.Selection([('cardio', 'Cardio'), ('weight', 'Weight')], default='cardio')
    quantity = fields.Integer()
