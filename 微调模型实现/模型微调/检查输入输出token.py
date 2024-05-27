import json

def count_tokens(text):
    # 直接计算文本中的字符数
    return len(text)

def calculate_average_tokens(file_path):
    total_prompt_tokens = 0
    total_response_tokens = 0
    total_entries = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line.strip())
            prompt = data.get("prompt", "")
            response = data.get("response", "")

            # 计算tokens
            total_prompt_tokens += count_tokens(prompt)
            total_response_tokens += count_tokens(response)
            total_entries += 1

    # 计算平均值并四舍五入到最近的整数
    average_prompt_tokens = round(total_prompt_tokens / total_entries)
    average_response_tokens = round(total_response_tokens / total_entries)

    return average_prompt_tokens, average_response_tokens

# 文件路径
file_path = "/root/微调地点/单轮.jsonl"

# 计算平均token数量
average_prompt, average_response = calculate_average_tokens(file_path)
print(f"输入平均 tokens: {average_prompt}")
print(f"输出平均 tokens: {average_response}")
