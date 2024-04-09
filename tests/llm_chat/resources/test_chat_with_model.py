# -*- coding: utf-8 -*-

import pytest
from bk_resource import api  # noqa
from mock import patch

from tests.constants import TEST_MODEL_UID

pytestmark = pytest.mark.django_db


class TestChatWithModel:
    """
    单元测试-测试模型对话交互接口
    """

    @pytest.fixture(autouse=True)
    def setup_method(self, bk_request, chat_with_model):
        self.chat_with_model = chat_with_model

    def test_chat_with_model(self):
        # 模拟请求数据
        validated_request_data = {
            "messages": [
                {"role": "user", "content": "Hello"},
                {"role": "user", "content": "How are you?"},
            ],
            "model": TEST_MODEL_UID,
        }

        # 模拟 `api.xinference.chat_with_model` 返回的数据
        mock_response = {
            "result": True,
            "data": {
                "messages": [
                    {"role": "user", "content": "Hello"},
                    {"role": "user", "content": "How are you?"},
                    {"role": "ai", "content": "I'm fine, thank you!"},
                ],
            },
        }

        # 模拟 `api.xinference.chat_with_model` 方法来返回上面定义的 mock_response
        with patch.object(api.xinference, "chat_with_model", return_value=mock_response) as mock_chat_with_model:
            response = self.chat_with_model(validated_request_data)

            # 验证模拟的方法被正确调用
            mock_chat_with_model.assert_called_once_with(
                messages=validated_request_data["messages"],
                model=validated_request_data["model"],
            )

            # 验证返回的数据与模拟的数据匹配
            assert response == mock_response
