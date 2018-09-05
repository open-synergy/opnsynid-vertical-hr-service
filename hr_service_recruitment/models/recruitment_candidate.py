# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class RecruitmentCandidate(models.Model):
    _name = "hr_service.recruitment_candidate"
    _description = "HR Service - Recruitment Candidate"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ["mail.thread"]

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        ondelete="cascade",
        )
    month_until_available = fields.Integer(
        string="Month Until Available",
        )
    expected_salary_currency_id = fields.Many2one(
        string="Expected Salary Currency",
        comodel_name="res.currency",
        )
    expected_salary = fields.Float(
        string="Expected Salary",
        )
    expected_field_of_work_id = fields.Many2one(
        string="Expected Field of Work",
        comodel_name="partner.field_of_work",
        )
    expected_job_level_id = fields.Many2one(
        string="Expected Job Level",
        comodel_name="partner.job_level",
        )
    expected_job_id = fields.Many2one(
        string="Expected Job",
        comodel_name="res.partner.job_position",
        )

    @api.multi
    def onchange_type(self, is_company):
        return self.partner_id.onchange_type(is_company)

    def onchange_address(self, cr, uid, ids, use_parent_address, parent_id, context=None):
        return self.partner_id.onchange_address(cr, uid, ids, use_parent_address, parent_id, context)

    @api.multi
    def onchange_state(self, state_id):
        return self.env["res.partner"].onchange_state(state_id)


