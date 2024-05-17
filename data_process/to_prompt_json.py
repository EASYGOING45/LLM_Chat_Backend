import json

# 输入和输出文件路径
input_file_path = './datasets/全新优质动漫数据集.txt'
output_file_path = 'output.jsonl'

# 读取txt文件内容
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 解析txt文件内容并转换为jsonl格式
jsonl_data = []
current_prompt = ''
current_response = ''
is_prompt = True

for line in lines:
    line = line.strip()
    if line.startswith('问：'):
        if current_prompt and current_response:
            jsonl_data.append({
                'prompt': current_prompt,
                'response': current_response
            })
        current_prompt = line[2:].strip()
        current_response = ''
        is_prompt = False
    elif line.startswith('答：'):
        current_response = line[2:].strip()
        is_prompt = False
    else:
        if is_prompt:
            current_prompt += ' ' + line
        else:
            current_response += ' ' + line

# 添加最后一个对话
if current_prompt and current_response:
    jsonl_data.append({
        'prompt': current_prompt,
        'response': current_response
    })

# 将数据写入jsonl文件
with open(output_file_path, 'w', encoding='utf-8') as file:
    for entry in jsonl_data:
        file.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"数据已成功转换并保存到 {output_file_path}")
