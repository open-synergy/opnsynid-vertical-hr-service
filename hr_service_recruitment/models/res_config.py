# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResConfig(models.TransientModel):
    _inherit = "hr_service.config_setting"

    recruitment_request_sequence_id = fields.Many2one(
        string="Recruitment Request Sequence",
        comodel_name="ir.sequence",
        related="company_id.recruitment_request_sequence_id",
        )
    recruitment_applicant_sequence_id = fields.Many2one(
        string="Recruitment Applicant Sequence",
        comodel_name="ir.sequence",
        related="company_id.recruitment_applicant_sequence_id",
        )
