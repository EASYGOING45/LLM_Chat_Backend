# -*- coding: utf-8 -*-

import pytest
from bk_resource import api  # noqa
from mock import patch

pytestmark = pytest.mark.django_db


class TestGetRunningModels:
    """
    单元测试-测试查询可用模型接口
    """

    @pytest.fixture(autouse=True)
    def setup_method(self, bk_request, get_running_models):
        self.get_running_models = get_running_models

    def test_get_running_models(self):
        # 模拟 `api.xinference.get_models_list` 返回的数据
        mock_response = {
            "result": True,
            "data": [
                {
                    "model_uid": "model_1",
                    "model_name": "Model 1",
                    "creator": "admin",
                    "create_time": "2020-01-01T00:00:00",
                },
                {
                    "model_uid": "model_2",
                    "model_name": "Model 2",
                    "creator": "admin",
                    "create_time": "2020-01-02T00:00:00",
                },
            ],
        }

        # 模拟 `api.xinference.get_models_list` 方法来返回上面定义的 mock_response
        with patch.object(api.xinference, "get_models_list", return_value=mock_response) as mock_get_models_list:
            response = self.get_running_models()

            # 验证模拟的方法被正确调用
            mock_get_models_list.assert_called_once()

            # 验证返回的数据与模拟的数据匹配
            assert response == mock_response
