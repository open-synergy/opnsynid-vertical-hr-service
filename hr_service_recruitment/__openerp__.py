# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Human Resource Service - Recruitment",
    "summary": "Manage Recruitment Service",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "website": "https://opensynergy-indonesia.com",
    "license": "AGPL-3",
    "depends": [
        "partner_contact_job_position",
        "hr_service_app",
        "partner_app",
        "mail",
        "partner_skill",
    ],
    "data": [
        "menu.xml",
        "views/hr_service_config_setting_views.xml",
        "views/recruitment_applicant_views.xml",
        "views/recruitment_request_views.xml",
        "views/recruitment_stage_views.xml",
        "views/recruitment_benefit_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
}
