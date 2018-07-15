# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class RecruitmentBenefit(models.Model):
    _name = "hr_service.recruitment_benefit"
    _description = "HR Service - Recruitment Benefit"

    name = fields.Char(
        string="Benefit",
        required=True,
        )
    active = fields.Boolean(
        string="Active",
        default=True,
        )
    description = fields.Text(
        string="Description",
        )
