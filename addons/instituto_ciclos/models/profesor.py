from odoo import fields, models


class InstitutoProfesor(models.Model):
    _name = "instituto.profesor"
    _description = "Profesor"

    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    numero_colegiado = fields.Char(required=True)
    modulo_ids = fields.One2many("instituto.modulo", "profesor_id", string="Modulos que imparte")

