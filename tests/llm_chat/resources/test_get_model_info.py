# -*- coding: utf-8 -*-

import pytest
from bk_resource import api  # noqa
from mock import patch

from tests.constants import TEST_MODEL_UID

pytestmark = pytest.mark.django_db


class TestGetModelInfo:
    """
    单元测试-测试查询模型详情信息接口
    """

    @pytest.fixture(autouse=True)
    def setup_method(self, bk_request, get_model_info):
        self.get_model_info = get_model_info

    def test_get_model_info(self):
        # 模拟请求数据
        validated_request_data = {
            "model_uid": TEST_MODEL_UID,
        }

        # 模拟 `api.xinference.get_model_info` 返回的数据
        mock_response = {
            "result": True,
            "data": {
                "model_uid": TEST_MODEL_UID,
                "model_name": "Model 1",
                "creator": "admin",
                "create_time": "2020-01-01T00:00:00",
            },
        }

        # 模拟 `api.xinference.get_model_info` 方法来返回上面定义的 mock_response
        with patch.object(api.xinference, "get_model_info", return_value=mock_response) as mock_get_model_info:
            response = self.get_model_info(validated_request_data)

            # 验证模拟的方法被正确调用
            mock_get_model_info.assert_called_once_with(model_uid=TEST_MODEL_UID)

            # 验证返回的数据与模拟的数据匹配
            assert response == mock_response
