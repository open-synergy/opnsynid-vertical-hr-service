# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class ApplicantDone(models.TransientModel):
    _name = "hr_service.applicant_done"
    _description = "Wizard to Accept Applicant"

    @api.model
    def _default_applicant_id(self):
        return self.env.context.get("active_id", False)

    applicant_id = fields.Many2one(
        string="Applicant",
        comodel_name="hr_service.recruitment_applicant",
        required=True,
        default=lambda self: self._default_applicant_id(),
    )


    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._confirm()

    @api.multi
    def _confirm(self):
        self.ensure_one()
