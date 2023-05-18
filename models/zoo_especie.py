from odoo import models, fields     
class zoo_animal(models.Model): 
    _name = 'zoo.animal' 
    id = fields.Integer('Id', required=True) 
    continentOrigen = fields.Char('Continent d''origen')     
    dataNaix = fields.Char('Data de naixement')     
    sexe = fields.Char('Sexe')