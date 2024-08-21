from odoo import models, fields, api


class Student(models.Model):
    _name = "educational_center.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    group_ids = fields.Many2many("educational_center.group", string="Groups")
    payment_ids = fields.One2many(
        "educational_center.payment", "student_id", string="Payments"
    )
