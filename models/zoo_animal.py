from odoo import models, fields     
class zoo_zoo(models.Model): 
    _name = 'zoo.zoo' 
    id = fields. Integer('Id', required=True) 
    nom = fields.Char('Nom', required=True)     
    grandaria = fields.Char('Grandaria')     
    ciutat = fields.Char('Ciutat')   
    pais = fields.Text('País')

    zoo_id = fields.Many2one('zoo.zoo',string='Zoo')

    especie_id = fields.Many2one('zoo.especie',string='Especie')