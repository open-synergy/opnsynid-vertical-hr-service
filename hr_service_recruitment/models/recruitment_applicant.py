# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError



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
        obj_request =\
            self.env["hr_service.recruitment_request"]
        stage_ids = []
        criteria = []

        request_id =\
            self._context.get('default_request_id', False)

        if request_id:
            criteria_request = [
                ("id", "=", request_id)
            ]
            request = obj_request.search(criteria_request)
            if request:
                for stage in request.stage_ids:
                    stage_ids.append(stage.stage_id.id)
                criteria = [
                    ("id", "in", stage_ids)
                ]
        stages =\
            self.env["hr_service.recruitment_stage"].search(
                criteria).name_get()

        return stages, None

    _group_by_full = {
        "stage_id": _stage_groups,
    }

    @api.model
    def create(self, values):
        _super = super(RecruitmentApplicant, self)
        result = _super.create(values)
        result.write(result._prepare_create_data())
        return result

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

        result = self.request_id._get_applicant_sequence()
        return result

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        return {
            "stage_id": self._get_first_open_stage().id,
            }

    @api.multi
    def _prepare_open_data(self):
        self.ensure_one()
        return {
            "stage_id": self._get_first_open_stage().id,
            }

    @api.multi
    def action_confirm(self):
        for applicant in self:
            applicant.write(self._prepare_confirm_data())

    @api.multi
    def action_next_open_stage(self):
        #TODO
        for applicant in self:
            applicant.write(self._prepare_open_data())

    @api.multi
    def action_previous_open_stage(self):
        #TODO
        for applicant in self:
            applicant.write(self._prepare_open_data())

    @api.multi
    def _get_first_open_stage(self):
        self.ensure_one()

        open_stages = self.request_id.\
            open_stage_ids

        if len(open_stages) == 0:
            raise UserError(_("No stage for open state"))

        return open_stages[0].stage_id



