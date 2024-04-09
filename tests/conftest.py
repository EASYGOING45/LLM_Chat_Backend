# -*- coding: utf-8 -*-
import os
import sys
import uuid

import pytest
from bk_resource import resource
from django.http import HttpRequest

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(here, "modules"))


@pytest.fixture(scope="session", autouse=True)
def bk_request():
    class Base(object):
        pass

    request = HttpRequest()
    request.user = Base()
    request.source = "WEB"
    request.user.username = "admin"
    request.user.is_superuser = True
    request.user.is_authenticated = True
    request.user.is_active = True

    request.session = {"bluking_timezone": "Asia/Shanghai"}

    request.permission_exempt = True
    request.META.update({"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"})

    # 获得请求唯一ID
    request.request_id = str(uuid.uuid4())


@pytest.fixture
def get_model_info():
    return resource.llm_chat.get_model_info


@pytest.fixture()
def get_running_models():
    return resource.llm_chat.get_running_models


@pytest.fixture()
def chat_with_model():
    return resource.llm_chat.chat_with_model


@pytest.fixture()
def get_users():
    return resource.user_manage.get_users


@pytest.fixture()
def update_user():
    return resource.user_manage.update_user
