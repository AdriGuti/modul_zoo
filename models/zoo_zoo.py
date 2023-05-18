from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    id = fields.Char('Id', required=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Date('Nom científic')
    nomVulgar = fields.Char('Nom vulgar')
    perill = fields.Char('Perill')