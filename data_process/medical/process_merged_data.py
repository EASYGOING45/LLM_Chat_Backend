import pandas as pd

# 尝试使用GBK编码读取questions.csv文件
try:
    questions_df = pd.read_csv('questions.csv', encoding='GBK')
except UnicodeDecodeError:
    print("无法使用GBK编码读取questions.csv文件，请检查文件编码或尝试其他编码。")
    raise

# 尝试读取answers_new.xlsx文件
try:
    answers_df = pd.read_excel('answers_new.xlsx')
except Exception as e:
    print(f"读取answers_new.xlsx文件时出错: {e}")
    raise

# 合并两个数据集，基于que_id列
merged_df = pd.merge(answers_df, questions_df, on='que_id')

# 按照big_cate分组
grouped = merged_df.groupby('big_cate')

# 为每个big_cate生成一个新的CSV文件
for name, group in grouped:
    # 选择需要的列
    result_df = group[['ques_content', 'ans_content']]
    # 生成文件名
    filename = f'{name}.csv'
    # 保存为CSV文件
    result_df.to_csv(filename, index=False, encoding='utf-8-sig')

print("CSV文件生成完毕。")
