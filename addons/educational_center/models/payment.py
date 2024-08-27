from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError



class Payment(models.Model):
    _name = "educational_center.payment"
    _description = "Payment"

    student_id = fields.Many2one(
        "educational_center.student", string="Student", required=True
    )
    amount = fields.Float(string="Amount", required=True)
    date = fields.Date(string="Date", default=fields.Date.today)
    note = fields.Text(string="Note")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
        ],
        string="Status",
        default="draft",
    )

    is_recent = fields.Boolean(
        string="Is Recent", compute="_compute_is_recent", store=True
    )
    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount <= 0:
                raise ValidationError("Payment amount must be positive.")

    @api.depends("create_date")
    def _compute_is_recent(self):
        seven_days_ago = datetime.now() - timedelta(days=7)
        for record in self:
            record.is_recent = record.create_date >= seven_days_ago

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_reset_to_draft(self):
        self.write({"state": "draft"})

    @api.model
    def get_last_week_payments(self):
        last_week = fields.Date.today() - timedelta(days=7)
        return self.search([('date', '>', last_week)])
