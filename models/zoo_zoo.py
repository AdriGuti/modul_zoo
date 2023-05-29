from odoo import models, fields     
class zoo_zoo(models.Model): 
    _name = 'zoo.zoo' 
    id = fields. Integer('Id', required=True) 
    nom = fields.Char('Nom', required=True)     
    grandaria = fields.Char('Grandaria')     
    ciutat = fields.Char('Ciutat')   
    pais = fields.Char('País')

    animals_id = fields.One2many('zoo.animal','zoo_id',string='Animals')