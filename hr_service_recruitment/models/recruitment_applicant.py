# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class RecruitmentApplicant(models.Model):
    _name = "hr_service.recruitment_applicant"
    _inherit = ["mail.thread"]
    _description = "HR Service - Recruitment Applicant"

    @api.model
    def _default_stage_id(self):
        #TODO
        return 1

    name = fields.Char(
        string="# Applicant",
        required=True,
        default="/",
        )
    request_id = fields.Many2one(
        string="# Recruitment Request",
        comodel_name="hr_service.recruitment_request",
        required=True,
        )
    applicant_id = fields.Many2one(
        string="Applicant",
        comodel_name="res.partner",
        required=True,
        domain=[
            ("is_company", "=", False),
            ("parent_id", "=", False),
            ("is_talent", "=", True),
            ],
        )
    date_applied = fields.Datetime(
        string="Date Applied",
        required=True,
        )
    note = fields.Text(
        string="Note",
        )
    stage_id = fields.Many2one(
        string="Stage",
        comodel_name="hr_service.recruitment_stage",
        required=True,
        default=lambda self: self._default_stage_id(),
        )
    state = fields.Selection(
        string="State",
        related="stage_id.state",
        selection=[
            ("new", "New"),
            ("open", "Open"),
            ("done", "Done"),
            ("cancel", "Cancel"),
            ("pending", "Pending"),
            ],
        store=True,
        )

    @api.multi
    def _stage_groups(self, domain, **kwargs):
        stages = self.env["hr_service.recruitment_stage"].search([]).name_get()

        return stages, None

    _groups_by_full = {
        "stage_id": _stage_groups,
        }
