from odoo import models, fields, api

class BulkPaymentConfirm(models.TransientModel):
    _name = 'educational_center.bulk_payment_confirm'
    _description = 'Bulk Payment Confirmation'

    payment_ids = fields.Many2many('educational_center.payment',
                                   'edu_bulk_payment_rel',
                                   'wizard_id',
                                   'payment_id',
                                   string='Payments to Confirm')

    @api.model
    def default_get(self, fields):
        res = super(BulkPaymentConfirm, self).default_get(fields)
        active_ids = self.env.context.get('active_ids', [])
        res['payment_ids'] = [(6, 0, active_ids)]
        return res

    def confirm_payments(self):
        for payment in self.payment_ids:
            payment.action_confirm()
        return {'type': 'ir.actions.act_window_close'}
