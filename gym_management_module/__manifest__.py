{
    'name': 'Gym Management',
    'version': '1.0',
    'summary': 'Manage gym memberships, classes, trainers, and equipment',
    'description': """
        This module allows you to manage a gym including memberships, classes, trainers, and equipment.
    """,
    'category': 'Tools',
    'author': 'abdi osman',
    'website': '#',
    'depends': ['base'],
    'data': [
        'views/gym_member_views.xml',
        'views/gym_trainer_views.xml',
        'views/gym_class_views.xml',
        'views/gym_equipment_views.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
