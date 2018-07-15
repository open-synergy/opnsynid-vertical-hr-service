# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class RecruitmentStage(models.Model):
    _name = "hr_service.recruitment_stage"
    _description = "HR Service - Recruitment Stage"

    name = fields.Char(
        string="Stage",
        required=True,
        )
    active = fields.Boolean(
        string="Active",
        default=True,
        )
    default_sequence = fields.Integer(
        string="Default Sequence",
        required=True,
        default=5,
        )
    description = fields.Text(
        string="Description",
        )
    state = fields.Selection(
        string="State",
        selection=[
            ("new", "New"),
            ("open", "Open"),
            ("done", "Done"),
            ("cancel", "Cancel"),
            ("pending", "Pending"),
            ],
        required=True,
        default="new",
        )
