# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    recruitment_request_sequence_id = fields.Many2one(
        string="Recruitment Request Sequence",
        comodel_name="ir.sequence",
        )

    recruitment_applicant_sequence_id = fields.Many2one(
        string="Recruitment Applicant Sequence",
        comodel_name="ir.sequence",
        )

    @api.multi
    def _get_applicant_sequence(self):
        self.ensure_one()

        if self.recruitment_applicant_sequence_id:
            result = self.recruitment_applicant_sequence_id
        else:
            result = self.env.ref(
                "hr_service_recruitment.sequence_hr_service_"
                "recruitment_applicant")
        return result
