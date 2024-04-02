# -*- coding: utf-8 -*-

import os

from api.constants import APIProvider
from api.utils import get_endpoint

# User Manage
USER_MANAGE_URL = get_endpoint("usermanage", APIProvider.ESB)

# Xinference
XINFERENCE_URL = os.getenv("BKAPP_LLM_API_ENDPOINT")
