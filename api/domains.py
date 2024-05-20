# -*- coding: utf-8 -*-

import os

from api.constants import APIProvider
from api.utils import get_endpoint

# User Manage
USER_MANAGE_URL = get_endpoint("usermanage", APIProvider.ESB)

# Xinference
XINFERENCE_URL = os.getenv("BKAPP_LLM_API_ENDPOINT")

# CLOSE_AI
CLOSE_AI_URL = os.getenv("BKAPP_CLOSE_API_ENDPOINT")

# 知识库
KNOWLEDGE_BASE_URL = os.getenv("BKAPP_KNOWLEDGE_BASE_URL")
