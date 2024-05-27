import dash
from dash import html, dcc, Input, Output
import plotly.graph_objs as go
import pandas as pd
import re
import os

# 正则表达式，用于从日志中提取数据
pattern = re.compile(r"\{'loss': ([\d.]+), 'learning_rate': ([\d.e-]+), 'epoch': ([\d.]+)\}")

# 创建一个Dash应用
app = dash.Dash(__name__)

# 应用布局
app.layout = html.Div([
    html.H1("模型微调实时监控", style={'textAlign': 'center'}),
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # 以毫秒为单位，10秒
        n_intervals=0
    )
])

# 从 hhh.txt 文件中读取模型名称
model_name_path = '/root/ChatGLM3/finetune_chatmodel_demo/hhh/hhh.txt'
try:
    with open(model_name_path, 'r') as file:
        model_name = file.read().strip()
    log_file_path = f'/root/微调地点/output/{model_name}/train.log'
except Exception as e:
    print(f"Error reading model name: {e}")
    exit(1)

# 回调函数，用于更新图表
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    data = {'epoch': [], 'loss': [], 'learning_rate': []}
    # 确保使用正确的日志文件路径
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    data['epoch'].append(float(match.group(3)))
                    data['loss'].append(float(match.group(1)))
                    data['learning_rate'].append(float(match.group(2)))

    df = pd.DataFrame(data)

    # 创建图表
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['epoch'], y=df['loss'],
                             mode='lines+markers',
                             name='Loss',
                             line=dict(color='firebrick', width=2),
                             marker=dict(size=6)))
    fig.add_trace(go.Scatter(x=df['epoch'], y=df['learning_rate'],
                             mode='lines+markers',
                             name='Learning Rate',
                             line=dict(color='royalblue', width=2),
                             marker=dict(size=6)))

    # 更新图表布局
    fig.update_layout(
        title='模型微调实时监控',
        xaxis_title='Epoch',
        yaxis_title='值',
        legend=dict(x=0, y=1, traceorder='normal'),
        margin=dict(l=40, r=0, t=40, b=30)
    )

    return fig

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True, port=6006)
