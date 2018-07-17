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

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id


    name = fields.Char(
        string="# Request",
        default="/",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        translate=False,
        default=lambda self: self._default_company_id(),
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date_request = fields.Datetime(
        string="Date Request",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    date_deadline = fields.Datetime(
        string="Date Deadline",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    partner_id = fields.Many2one(
        string="Customer",
        comodel_name="res.partner",
        required=True,
        domain="[('is_company','=',True),('parent_id', '=', False)]",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    request_by_id = fields.Many2one(
        string="Request By",
        comodel_name="res.partner",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    job_id = fields.Many2one(
        string="Position",
        comodel_name="res.partner.job_position",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    job_location_id = fields.Many2one(
        string="Job Placement",
        comodel_name="res.partner",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    no_of_recruitment = fields.Integer(
        string="Expected New Employee",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
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
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    required_skill_ids = fields.Many2many(
        string="Required Skill",
        comodel_name="hr.skill",
        relation="rel_recruitment_request_required_skill",
        column1="request_id",
        column2="skill_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    nice_to_have_skill_ids = fields.Many2many(
        string="Nice to Have Skill",
        comodel_name="hr.skill",
        relation="rel_recruitment_request_nice_to_have_skill",
        column1="request_id",
        column2="skill_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    min_year_experience = fields.Float(
        string="Minimum Years Experiences",
        required=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    salary_currency_id = fields.Many2one(
        string="Salary Currency",
        comodel_name="res.currency",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    min_salary = fields.Float(
        string="Min. Salary",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    max_salary = fields.Float(
        string="Max. Salary",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        )
    benefit_ids = fields.Many2many(
        string="Benefits",
        comodel_name="hr_service.recruitment_benefit",
        relation="rel_recruitment_request_2_benefit",
        column1="request_id",
        column2="benefit_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
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
        for recruitment in self:
            recruitment.write(self._prepare_approve_data())

    @api.multi
    def action_done(self):
        for recruitment in self:
            recruitment.write(self._prepare_done_data())

    @api.multi
    def action_cancel(self):
        for recruitment in self:
            recruitment.write(self._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        for recruitment in self:
            recruitment.write(self._prepare_restart_data())

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        return {
            "state": "confirm",
            }

    @api.multi
    def _prepare_approve_data(self):
        self.ensure_one()
        return {
            "state": "approve",
            }

    @api.multi
    def _prepare_done_data(self):
        self.ensure_one()
        return {
            "state": "done",
                }

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        return {
            "state": "cancel",
            }

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        return {
            "state": "draft",
            }

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
        self.ensure_one()
        company = self.company_id

        if company.recruitment_request_sequence_id:
            result = company.recruitment_request_sequence_id
        else:
            result = self.env.ref(
                "hr_service_recruitment.sequence_hr_service_"
                "recruitment_request")
        return result

    @api.model
    def create(self, values):
        _super = super(RecruitmentRequest, self)
        result = _super.create(values)
        result.write(result._prepare_create_data())
        return result

    @api.onchange("partner_id")
    def onchange_request_by_id(self):
        self.request_by_id = False
        domain = {
            "request_by_id": [
                ("id", "=", 0),
                ],
            }
        if self.partner_id:
            domain["request_by_id"] = [
                ("commercial_partner_id", "=", self.partner_id.id),
                ("is_company", "=", False),
                ("type", "=", "contact"),
                ]
        return {"domain": domain}

    @api.onchange("partner_id")
    def onchange_job_location_id(self):
        self.job_location_id = False
        domain = {
            "job_location_id": [
                ("id", "=", 0),
                ],
            }
        if self.partner_id:
            domain["job_location_id"] = [
                ("commercial_partner_id", "=", self.partner_id.id),
                ("is_company", "=", False),
                ("type", "!=", "contact"),
                ]
        return {"domain": domain}

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
