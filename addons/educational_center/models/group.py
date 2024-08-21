from odoo import models, fields, api


class Group(models.Model):
    _name = "educational_center.group"
    _description = "Group"

    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one(
        "educational_center.course", string="Course", required=True
    )
    teacher_ids = fields.Many2many("educational_center.teacher", string="Teachers")
    student_ids = fields.Many2many("educational_center.student", string="Students")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
