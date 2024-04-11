# -*- coding: utf-8 -*-

import pytest
from blueapps.account.models import User

pytestmark = pytest.mark.django_db


class TestUpdateUser:
    """
    单元测试-测试更新用户信息接口
    """

    @pytest.fixture(autouse=True)
    def setup_method(self, bk_request, update_user):
        self.update_user = update_user

    def test_update_user(self):
        # 创建测试用户
        test_user = User.objects.create_user(username="test_user", password="test_password")

        # 模拟请求数据
        validated_request_data = {
            "username": "test_user",
        }

        # 调用接口方法更新用户信息
        response = self.update_user(validated_request_data)

        # 验证返回的数据与更新后的用户信息匹配
        assert response == {
            "username": "test_user",
            "is_staff": True,
            "is_active": True,
            "is_superuser": True,
        }

        # 清理测试用户
        test_user.delete()
