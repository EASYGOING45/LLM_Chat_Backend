import os
import requests
from bs4 import BeautifulSoup
import csv

# 定义目标URL的模板
url_template = "https://www.iamshuaidi.com/{}.html"

# 创建一个用于存储CSV文件的目录
output_dir = 'interview_questions_new'
os.makedirs(output_dir, exist_ok=True)

# 爬取从1到5000中的有数据的面试题
for i in range(5500, 10000):
    url = url_template.format(i)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # 获取题目
        title_tag = soup.find('meta', attrs={'property': 'og:title'})
        if title_tag:
            title = title_tag['content'].replace('-帅地玩编程', '').strip()
        else:
            continue

        # 获取分类
        keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
        if keywords_tag:
            category = keywords_tag['content'].split(',')[0].strip()
        else:
            continue

        # 获取回答内容
        content_div = soup.find('div', class_='entry-content')
        if content_div:
            paragraphs = content_div.find_all(['p', 'a'])
            answer = "\n".join([p.get_text() for p in paragraphs]).strip()

            # 去除水印
            unwanted_phrases = ["计算机网络面试题", "帅地永久会员"]
            for phrase in unwanted_phrases:
                answer = answer.replace(phrase, "").strip()
        else:
            continue

        # 确定分类对应的CSV文件路径
        csv_file_path = os.path.join(output_dir, f'{category}.csv')

        # 检查CSV文件是否存在，如果不存在则创建并写入表头
        file_exists = os.path.isfile(csv_file_path)
        with open(csv_file_path, 'a', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['问题', '回答', '所属分类']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            # 写入数据
            writer.writerow({'问题': title, '回答': answer})
            print(f"已成功爬取：{url} ,问题{title},并存储到 {csv_file_path}")

print("爬取完毕")
