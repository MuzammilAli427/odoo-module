# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class MyModel(models.Model):
    _name = "my.database"

    first_name = fields.Char()
    last_name = fields.Char()
    p_id = fields.Char()
    payment = fields.Char()
