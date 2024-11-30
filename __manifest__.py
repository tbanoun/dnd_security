{
    "name": "DND Security",
    "summary": """""",
    "version": "17.0.0.1",
    "license": "AGPL-3",
    "author": "BANOUN Tahar/ DND Counsulting GROUP",
    "website": "https://dndconsulting.dz/",
    "depends": ["simplify_access_management", "contacts_dnd"],
    "data": [
        # security
        'security/ir.model.access.csv',
        'security/security_group.xml',
        'security/security_rule_admin.xml',
        'security/security_rule_user.xml',
        'security/generale_ir_rule.xml',
        'security/security_rule_team_leader.xml',


        # views
        'views/res_partner.xml',
        'views/main_menu.xml',
    ],
    "installable": True,
}
