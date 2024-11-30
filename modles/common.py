def checkUserHasGroup(self, group):
    """"
     Vérifie si l'utilisateur actuel appartient à un groupe spécifique dans Odoo
    """
    user = self.env.user
    if user.has_group(group): return True
    return False
