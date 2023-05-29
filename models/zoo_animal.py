from odoo import models, fields     
class zoo_animal(models.Model): 
    _name = 'zoo.animal' 
    id = fields.Integer('Id', required=True) 
    continentOrigen = fields.Char('Continent d''origen')     
    dataNaix = fields.Char('Data de naixement')     
    sexe = fields.Char('Sexe')

    zoo_id = fields.Many2one('zoo.zoo',string='Zoo')

    especie_id = fields.Many2one('zoo.especie',string='Especie')