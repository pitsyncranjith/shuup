# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import django.conf

from shuup.apps import AppConfig
from shuup.apps.settings import validate_templates_configuration


class ShuupFrontAppConfig(AppConfig):
    name = "shuup.front"
    verbose_name = "Shuup Frontend"
    label = "shuup_front"

    provides = {
        "front_extend_product_list_form": [
            "shuup.front.forms.product_list_modifiers.SortProductListByCreatedDate",
            "shuup.front.forms.product_list_modifiers.SortProductListByName",
        ],
    }

    def ready(self):
        validate_templates_configuration()
        if django.conf.settings.SHUUP_FRONT_INSTALL_ERROR_HANDLERS:
            from .error_handling import install_error_handlers
            install_error_handlers()


default_app_config = "shuup.front.ShuupFrontAppConfig"
