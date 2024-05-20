import os
import pandas as pd

# 定义要分类的关键字
keywords = ["C++", "Golang", "Go开发", "Java", "HTML", "Linux", "MyBatis", "mysql", "Python", "Redis",
            "Spring", "Vue", "Zookeeper", "前端", "大厂", "字节跳动", "算法", "计算机网络","面试","操作系统"]

# 创建新的文件夹用于存放合并后的CSV文件
merged_folder = "merged_csv_files"
if not os.path.exists(merged_folder):
    os.makedirs(merged_folder)

# 获取当前目录中的所有CSV文件
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# 对CSV文件进行分类并合并
for keyword in keywords:
    combined_df = pd.DataFrame()

    for csv_file in csv_files:
        if keyword in csv_file:
            df = pd.read_csv(csv_file)
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    # 如果有文件被合并，则保存合并后的文件
    if not combined_df.empty:
        combined_csv_path = os.path.join(merged_folder, f"{keyword}_combined.csv")
        combined_df.to_csv(combined_csv_path, index=False, encoding='utf-8-sig')
        print(f"合并后的文件已保存到: {combined_csv_path}")

print("所有文件合并完成。")
