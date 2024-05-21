import requests
import json

base_url = "http://localhost:6006"  # 把这里改成你的IP地址


def create_chat_completion(model, messages, use_stream=False):
    data = {
        "model": model,  # 模型名称
        "messages": messages,  # 会话历史
        "stream": use_stream,  # 是否流式响应
        "max_tokens": 100,  # 最多生成字数
        "temperature": 0.8,  # 温度
        "top_p": 0.8,  # 采样概率
    }

    response = requests.post(f"{base_url}/v1/chat/completions", json=data, stream=use_stream)
    if response.status_code == 200:
        if use_stream:
            # 处理流式响应
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')[6:]
                    try:
                        response_json = json.loads(decoded_line)
                        content = response_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        print(content)
                    except:
                        print("Special Token:", decoded_line)
        else:
            # 处理非流式响应
            decoded_line = response.json()
            content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
            return content
    else:
        print("Error:", response.status_code)
        return None


if __name__ == "__main__":
    chat_messages = [
        {
            "role": "system",
            "content": "从现在开始扮演一个外冷内热的人和我对话",
        }
    ]

    while True:
        user_input = input("请输入您的问题: ")
        chat_messages.append({"role": "user", "content": user_input})
        response = create_chat_completion("chatglm3-6b", chat_messages, use_stream=False)
        print("回复:", response)
        # 可以选择是否在每次循环后清除聊天历史
        # chat_messages.pop()
