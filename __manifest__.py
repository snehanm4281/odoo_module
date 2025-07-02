{
    'name': 'Real Estate Management',
    'version': '1.0',
    'summary': 'Manage real estate properties',
    'description': 'Module to manage properties, owners, buyers and property status.',
    'category': 'Real Estate',
    'author': 'name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    'installable': True,
    'application': True,
}
