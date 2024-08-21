from odoo import models, fields, api


class Course(models.Model):
    _name = "educational_center.course"
    _description = "Course"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    teacher_ids = fields.Many2many("educational_center.teacher", string="Teachers")
    group_ids = fields.One2many(
        "educational_center.group", "course_id", string="Groups"
    )
