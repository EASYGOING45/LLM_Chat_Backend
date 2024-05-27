import os
import re
import subprocess

def find_max_numbered_subdirectory(parent_path):
    max_number = -1
    max_numbered_directory = None

    for entry in os.listdir(parent_path):
        path = os.path.join(parent_path, entry)
        if os.path.isdir(path) and not entry.startswith('.'):
            # 尝试从文件夹名中提取数字
            match = re.search(r'(\d+)$', entry)
            if match:
                number = int(match.group(1))
                if number > max_number:
                    max_number = number
                    max_numbered_directory = entry

    return max_numbered_directory

def list_directories_and_run_command(base_path, model_path, selected_directory_name=None):
    try:
        entries = os.listdir(base_path)
        directories = [entry for entry in entries if os.path.isdir(os.path.join(base_path, entry)) and not entry.startswith('.')]

        if directories:
            for directory in directories:
                # 如果指定了特定的目录，只处理该目录
                if selected_directory_name and directory != selected_directory_name:
                    continue

                full_directory_path = os.path.join(base_path, directory)
                max_subdirectory = find_max_numbered_subdirectory(full_directory_path)

                checkpoint_path = os.path.join(full_directory_path, max_subdirectory) if max_subdirectory else full_directory_path
                
                command = f"python inference.py --pt-checkpoint \"{checkpoint_path}\" --model {model_path}"
                print("正在执行命令: " + command)
                subprocess.run(command, shell=True)
                return
        else:
            print("在路径 '{}' 下没有找到任何非隐藏文件夹。".format(base_path))

    except Exception as e:
        print("无法访问路径 '{}'. 错误信息: {}".format(base_path, e))

model_name_path = '/root/ChatGLM3/finetune_chatmodel_demo/hhh/hhh.txt'
try:
    with open(model_name_path, 'r') as file:
        model_name = file.read().strip()
except Exception as e:
    print(f"Error reading model name: {e}")
    exit(1)

# 示例用法
base_path = '/root/微调地点/output'
model_path = '/root/autodl-tmp/chatglm3-6b'
list_directories_and_run_command(base_path, model_path, model_name)