import json
import math


# 读取JSONL文件
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line.strip()))
    return data


# 转换并拆分为多个TXT文件
def convert_and_split_to_txt(data, output_file_prefix, num_files):
    total_entries = len(data)
    entries_per_file = math.ceil(total_entries / num_files)

    for i in range(num_files):
        start_index = i * entries_per_file
        end_index = min((i + 1) * entries_per_file, total_entries)
        output_file_path = f"{output_file_prefix}_part_{i + 1}.txt"

        with open(output_file_path, 'w', encoding='utf-8') as file:
            for qa_pair in data[start_index:end_index]:
                prompt = qa_pair["prompt"]
                response = qa_pair["response"]
                file.write(f"问题：\n{prompt}\n\n回答：\n{response}\n\n")

        print(f"已将数据转换并保存到 {output_file_path}")


if __name__ == "__main__":
    input_file_path = '../depression_qa.jsonl'
    output_file_prefix = 'depression_qa'
    num_files = 4

    data = read_jsonl(input_file_path)
    convert_and_split_to_txt(data, output_file_prefix, num_files)
