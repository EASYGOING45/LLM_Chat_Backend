import json


# 读取数据集文件
def read_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


# 转换数据格式
def convert_to_qa_format(lines):
    qa_pairs = []
    i = 0
    while i < len(lines):
        prompt = lines[i].strip()
        response = lines[i + 1].strip()
        qa_pairs.append({"prompt": prompt, "response": response})
        i += 2  # 每次跳过两行
    return qa_pairs


# 保存到jsonl文件
def save_to_jsonl(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')


if __name__ == "__main__":
    dataset_file_path = '../datasets/huge'  # 假设数据集存储在这个文件中
    output_file_path = '../depression_qa.jsonl'

    lines = read_dataset(dataset_file_path)
    qa_pairs = convert_to_qa_format(lines)
    save_to_jsonl(qa_pairs, output_file_path)
    print(f"已生成数据并保存到 {output_file_path}")
