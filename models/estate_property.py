from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ], string='Property Type', default='house')
    address = fields.Char(string='Address')
    postcode = fields.Char(string='Postal Code')
    price = fields.Float(string='Price')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    ], string='Status', default='draft')
    owner_id = fields.Many2one('res.partner', string='Owner')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    active = fields.Boolean(string='Active', default=True)
