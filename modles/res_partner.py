from odoo import api, models, fields
from .common import *

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def actionReturnViewFormRequestCreation(self, res_id):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'dnd_security.action_contacts_request_cration')
        action["res_id"] = res_id
        return action


    def create(self, vals_list):
        # check user has privilage admin
        admin = checkUserHasGroup(self, 'dnd_security.admin_group_contact')
        if not admin: vals_list['active'] = False
        else: vals_list['active'] = True
        res = super(ResPartner, self).create(vals_list)
        return res


    def action_confirm(self):
        print("Confirm ok!")
        pass

    def action_cancel(self):
        print("Delete OK!")
        pass