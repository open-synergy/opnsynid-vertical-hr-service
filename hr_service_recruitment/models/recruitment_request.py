# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class RecruitmentRequest(models.Model):
    _name = "hr_service.recruitment_request"
    _inherit = ["mail.thread"]
    _description = "HR Service - Recruitment Request"

    @api.multi
    @api.depends("applicant_ids", "applicant_ids.stage_id")
    def _compute_applicant(self):
        for request in self:
            applicant_count = accepted_applicant_count = \
                rejected_applicant_count = 0
            request.applicant_count = applicant_count
            request.accepted_applicant_count = accepted_applicant_count
            request.rejected_applicant_count = rejected_applicant_count


    name = fields.Char(
        string="# Request",
        default="/",
        )
    date_request = fields.Datetime(
        string="Date Request",
        required=True,
        )
    date_deadline = fields.Datetime(
        string="Date Deadline",
        )
    partner_id = fields.Many2one(
        string="Customer",
        comodel_name="res.partner",
        required=True,
        domain="[('is_company','=',True),('parent_id', '=', False)]"
        )
    request_by_id = fields.Many2one(
        string="Request By",
        comodel_name="res.partner",
        required=True,
        )
    job_id = fields.Many2one(
        string="Position",
        comodel_name="res.partner.job_position",
        required=True,
        )
    job_location_id = fields.Many2one(
        string="Job Placement",
        comodel_name="res.partner",
        )
    no_of_recruitment = fields.Integer(
        string="Expected New Employee",
        )
    applicant_ids = fields.One2many(
        string="Applicants",
        comodel_name="hr_service.recruitment_applicant",
        inverse_name="request_id",
        )
    applicant_count = fields.Integer(
        string="Number of Applicant",
        compute="_compute_applicant",
        store=False,
        )
    accepted_applicant_count = fields.Integer(
        string="Number of Accepted Applicant",
        compute="_compute_applicant",
        store=False,
        )
    rejected_applicant_count = fields.Integer(
        string="Number of Rejected Applicant",
        compute="_compute_applicant",
        store=False,
        )
    stage_ids = fields.One2many(
        string="Stages",
        comodel_name="hr_service.recruitment_request_stage",
        inverse_name="request_id",
        )
    required_skill_ids = fields.Many2many(
        string="Required Skill",
        comodel_name="hr.skill",
        relation="rel_recruitment_request_required_skill",
        column1="request_id",
        column2="skill_id",
        )
    nice_to_have_skill_ids = fields.Many2many(
        string="Nice to Have Skill",
        comodel_name="hr.skill",
        relation="rel_recruitment_request_nice_to_have_skill",
        column1="request_id",
        column2="skill_id",
        )
    min_year_experience = fields.Float(
        string="Minimum Years Experiences",
        required=False,
        )
    salary_currency_id = fields.Many2one(
        string="Salary Currency",
        comodel_name="res.currency",
        )
    min_salary = fields.Float(
        string="Min. Salary",
        )
    max_salary = fields.Float(
        string="Max. Salary",
        )
    benefit_ids = fields.Many2many(
        string="Benefits",
        comodel_name="hr_service.recruitment_benefit",
        relation="rel_recruitment_request_2_benefit",
        column1="request_id",
        column2="benefit_id",
        )
    note = fields.Text(
        string="Note",
        )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("approve", "Open"),
            ("done", "Done"),
            ("cancel", "Cancel"),
            ],
        default="draft",
        required=True,
        )

    @api.multi
    def action_confirm(self):
        #TODO:
        for recruitment in self:
            recruitment.write(self._prepare_confirm_data())

    @api.multi
    def action_approve(self):
        #TODO:
        for recruitment in self:
            recruitment.write(self._prepare_approve_data())

    @api.multi
    def action_done(self):
        #TODO:
        for recruitment in self:
            recruitment.write(self._prepare_done_data())

    @api.multi
    def action_cancel(self):
        #TODO:
        for recruitment in self:
            recruitment.write(self._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        #TODO:
        for recruitment in self:
            recruitment.write(self._prepare_restart_data())

    @api.multi
    def _prepare_confirm_data(self):
        #TODO
        self.ensure_one()
        return {}

    @api.multi
    def _prepare_approve_data(self):
        #TODO
        self.ensure_one()
        return {}

    @api.multi
    def _prepare_done_data(self):
        #TODO
        self.ensure_one()
        return {}

    @api.multi
    def _prepare_cancel_data(self):
        #TODO
        self.ensure_one()
        return {}

    @api.multi
    def _prepare_restart_data(self):
        #TODO
        self.ensure_one()
        return {}

    @api.multi
    def _prepare_create_data(self):
        self.ensure_one()
        result = {}
        if self.name == "/":
            result.update({"name": self._create_sequence()})
        return result

    @api.multi
    def _create_sequence(self):
        self.ensure_one()
        name = self.env["ir.sequence"].\
            next_by_id(self._get_sequence().id) or "/"
        return name

    @api.multi
    def _get_sequence(self):
        #TODO
        self.sensure_one()
        pass

    @api.model
    def create(self, values):
        _super = super(RecruitmentRequest, self)
        result = _super.create(values)
        result.write(result._prepare_create_data())
        return result

    @api.onchange("partner_id")
    def onchange_request_by_id(self):
        #TODO
        pass

    @api.constrains("date_request", "date_deadline")
    def _check_date(self):
        #TODO
        pass

class RecruitmentRequestStage(models.Model):
    _name = "hr_service.recruitment_request_stage"
    _description = "HR Service - Stages of Recruitment Request"
    _order = "sequence, id"

    request_id = fields.Many2one(
        string="# Request",
        comodel_name="hr_service.recruitment_request",
        required=True,
        )
    stage_id = fields.Many2one(
        string="Stage",
        comodel_name="hr_service.recruitment_stage",
        required=True,
        )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
        )
