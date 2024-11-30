from odoo import api, models, fields
from odoo.tools.safe_eval import datetime
from .common import *
from datetime import datetime

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def actionReturnViewFormRequestCreation(self, res_id):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'dnd_security.action_contacts_request_cration')
        action["res_id"] = res_id
        return action

    def renderCrmLeadFormPage(self, res_id):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'crm.crm_lead_action_pipeline')
        action["res_id"] = res_id
        action["view_mode"] = 'form'
        return action


    def create(self, vals_list):
        # check user has privilage admin
        try:
            admin = checkUserHasGroup(self, 'dnd_security.admin_group_contact')
            if not admin:
                vals_list['active'] = False
                vals_list['user_id'] = self.env.user.id
            else: vals_list['active'] = True
        except Exception as e:
            print(e)
        res = super(ResPartner, self).create(vals_list)
        return res


    def action_confirm(self):
        self.active = True
        # créer une opportunité
        year = datetime.now().year
        vals = {
            "name": "New Lead %s" % self.display_name,
            "partner_id": self.id,
            "type": "opportunity",
            "year": year,
            'user_id': self.create_uid.id
        }
        res = self.env['crm.lead'].sudo().create(
            vals
        )
        action = self.renderCrmLeadFormPage(res.id)
        return action

    def action_cancel(self):
        notification = show_notification('success', 'Information', f'Le contact {self.display_name} a été supprimé avec succès.')
        self.sudo().unlink()
        return notification