from odoo import models, fields, api


class Teacher(models.Model):
    _name = "educational_center.teacher"
    _description = "Teacher"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    course_ids = fields.Many2many("educational_center.course", string="Courses")
    group_ids = fields.Many2many("educational_center.group", string="Groups")
