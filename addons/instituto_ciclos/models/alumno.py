from odoo import fields, models


class InstitutoAlumno(models.Model):
    _name = "instituto.alumno"
    _description = "Alumno"

    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    modulo_ids = fields.Many2many(
        "instituto.modulo",
        "instituto_modulo_alumno_rel",
        "alumno_id",
        "modulo_id",
        string="Modulos matriculados",
    )

