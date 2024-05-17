import json
import random

# 更大的示例问题和答案库
example_qa_pairs = [
    {
        "prompt": "什么是面向对象编程（OOP）？",
        "response": "面向对象编程（OOP）是一种编程范式，使用对象和类来组织代码。它的核心概念包括封装、继承、多态和抽象。"
    },
    {
        "prompt": "解释一下TCP/IP协议。",
        "response": "TCP/IP是互联网的基础协议，负责数据传输和通信。TCP负责数据传输的可靠性，IP负责数据包的路由。"
    },
    {
        "prompt": "什么是数据库索引？",
        "response": "数据库索引是一种数据结构，用于快速查找和检索数据库表中的数据。常见的索引类型包括B树索引和哈希索引。"
    },
    {
        "prompt": "解释一下进程和线程的区别。",
        "response": "进程是操作系统中运行的独立程序实例，拥有独立的内存空间。线程是进程中的一个执行单元，共享进程的内存空间。"
    },
    {
        "prompt": "什么是递归？",
        "response": "递归是一种编程技术，函数通过调用自身来解决问题。递归通常用于解决分治问题，如阶乘计算和斐波那契数列。"
    },
    {
        "prompt": "什么是数据库事务？",
        "response": "数据库事务是一组操作的集合，这些操作要么全部成功，要么全部失败。事务具有原子性、一致性、隔离性和持久性（ACID）。"
    },
    {
        "prompt": "解释一下HTTP和HTTPS的区别。",
        "response": "HTTP（超文本传输协议）是一种用于传输网页数据的协议。HTTPS（安全超文本传输协议）是在HTTP的基础上增加了SSL/TLS加密，以确保数据传输的安全性。"
    },
    {
        "prompt": "什么是RESTful API？",
        "response": "RESTful API是一种基于REST（表述性状态转移）架构风格的API设计方法。它使用HTTP请求方法（如GET、POST、PUT、DELETE）进行操作，通常返回JSON或XML格式的数据。"
    },
    {
        "prompt": "解释一下二叉树和二叉搜索树的区别。",
        "response": "二叉树是一种每个节点最多有两个子节点的数据结构。二叉搜索树是一种特殊的二叉树，其中每个节点的左子节点的值小于该节点的值，右子节点的值大于该节点的值。"
    },
    {
        "prompt": "什么是Docker？",
        "response": "Docker是一种开源平台，用于开发、部署和运行应用程序。它使用容器技术将应用程序及其依赖项打包在一起，实现一致的运行环境。"
    },
    # 添加更多问题和答案以确保多样性
]


# 生成不重复的数据集
def generate_unique_data(num_samples, qa_pairs):

    # 随机打乱QA对
    random.shuffle(qa_pairs)

    # 选择前num_samples个QA对
    data = qa_pairs[:num_samples]

    return data


# 保存到jsonl文件
def save_to_jsonl(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')


# 主函数
if __name__ == "__main__":
    num_samples = 1000

    generated_data = generate_unique_data(num_samples, example_qa_pairs)
    save_to_jsonl(generated_data, 'computer_interview_qa.jsonl')
    print(f"已生成 {num_samples} 条不重复的数据并保存到 computer_interview_qa.jsonl")
