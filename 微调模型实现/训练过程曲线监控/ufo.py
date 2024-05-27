import os
import subprocess

# 检查目标文件夹是否存在
folder_exists = os.path.exists('/root/autodl-tmp/chatglm3-6b')

# 如果目标文件夹不存在，则移动文件夹
if not folder_exists:
    subprocess.run(["mv", "/root/chatglm3-6b", "/root/autodl-tmp/"], check=True)

# 执行 Python 脚本
subprocess.run(["python", "/root/ChatGLM3/basic_demo/cli_demo.py"], check=True)
