from odoo import _

def checkUserHasGroup(self, group):
    """"
     Vérifie si l'utilisateur actuel appartient à un groupe spécifique dans Odoo
    """
    user = self.env.user
    if user.has_group(group): return True
    return False


def show_notification(status,title, message):
    """"""
    notification = {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': _(f'{title}'),
            'type': f'{status}',
            'message': f"{message}",
            'sticky': False,
        }
    }
    return notification