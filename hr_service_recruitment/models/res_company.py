# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    recruitment_request_sequence_id = fields.Many2one(
        string="Recruitment Request Sequence",
        comodel_name="ir.sequence",
        )
