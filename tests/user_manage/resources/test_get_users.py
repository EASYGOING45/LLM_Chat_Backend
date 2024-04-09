# -*- coding: utf-8 -*-

import pytest
from blueapps.account.models import User
from mock import patch  # noqa

pytestmark = pytest.mark.django_db


class TestGetUsers:
    """
    单元测试-测试获取用户信息接口
    """

    @pytest.fixture(autouse=True)
    def setup_method(self, bk_request, get_users):
        self.get_users = get_users

    def test_get_users(self):
        # 创建测试用户
        test_user_1 = User.objects.create_user(username="test_user_1", password="test_password")
        test_user_2 = User.objects.create_user(username="test_user_2", password="test_password")

        # 调用接口方法获取用户数据
        response = self.get_users()

        # 验证返回的数据包含创建的测试用户
        assert len(response) >= 2
        assert {"username": "test_user_1", "is_staff": False, "is_active": True, "is_superuser": False} in response
        assert {"username": "test_user_2", "is_staff": False, "is_active": True, "is_superuser": False} in response

        # 清理测试用户
        test_user_1.delete()
        test_user_2.delete()
