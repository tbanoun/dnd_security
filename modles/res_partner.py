from odoo import api, models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'


    def action_confirm(self):
        print("Confirm ok!")
        pass

    def action_cancel(self):
        print("Delete OK!")
        pass