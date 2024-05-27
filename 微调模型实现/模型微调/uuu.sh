#! /usr/bin/env bash

# 激活Python环境
source activate py310_chat
# 进入工作目录
cd /root/ChatGLM3/finetune_chatmodel_demo

# 只显示错误信息
set -e

# 默认参数
PRE_SEQ_LEN=128
LR=2e-2
NUM_GPUS=1
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=32
RUN_NAME=模型
BASE_MODEL_PATH=/root/autodl-tmp/chatglm3-6b
DATASET_PATH=/root/微调地点/单轮.jsonl

# 从先前的脚本中获取平均输入和输出token数，并分别加上128
# 假设先前的脚本保存在calculate_average_tokens.sh，并且输出格式为"输入平均 tokens: X 输出平均 tokens: Y"
TOKENS=$(python /root/微调地点/检查输入输出token.py)  # 替换为先前脚本的实际路径
AVERAGE_PROMPT=$(echo $TOKENS | grep -oP '输入平均 tokens: \K\d+')
AVERAGE_RESPONSE=$(echo $TOKENS | grep -oP '输出平均 tokens: \K\d+')

# 计算新的MAX_SOURCE_LEN和MAX_TARGET_LEN
MAX_SOURCE_LEN=$(($AVERAGE_PROMPT + 100))
MAX_TARGET_LEN=$(($AVERAGE_RESPONSE + 100))

# 从用户那里获取 MAX_STEP 和 SAVE_INTERVAL
echo -n "你想微调多少步: "
read MAX_STEP

echo -n "你想多少步保存一次: "
read SAVE_INTERVAL

# 显示感谢信息
echo "感谢你的使用，希望你可以微调出一个完美的模型！"

# 以流式输出显示ASCII艺术猫
function draw_cat() {
    sleep 0.05; echo "                  ******       ******"
    sleep 0.05; echo "                **      **   **      **"
    sleep 0.05; echo "              **         ** **         **"
    sleep 0.05; echo "             **          /\_/\          **"
    sleep 0.05; echo "             **         ( o.o )         **"
    sleep 0.05; echo "              **         > ^ <         **"
    sleep 0.05; echo "                **         v         **"
    sleep 0.05; echo "                  **               **"
    sleep 0.05; echo "                    **           **"
    sleep 0.05; echo "                      **       **"
    sleep 0.05; echo "                        **   **"
    sleep 0.05; echo "                          **"
}

draw_cat

# 设置输出目录
DATESTR=$(date +%s)
OUTPUT_DIR_NAME=${RUN_NAME}-${DATESTR}
OUTPUT_DIR=/root/微调地点/output/${OUTPUT_DIR_NAME}

# 创建必要的目录
mkdir -p /root/ChatGLM3/finetune_chatmodel_demo/hhh/
echo $OUTPUT_DIR_NAME > /root/ChatGLM3/finetune_chatmodel_demo/hhh/hhh.txt
mkdir -p $OUTPUT_DIR

# 运行微调脚本
torchrun --standalone --nnodes=1 --nproc_per_node=$NUM_GPUS finetune.py \
    --train_format input-output \
    --train_file $DATASET_PATH \
    --preprocessing_num_workers 1 \
    --model_name_or_path $BASE_MODEL_PATH \
    --output_dir $OUTPUT_DIR \
    --max_source_length $MAX_SOURCE_LEN \
    --max_target_length $MAX_TARGET_LEN \
    --per_device_train_batch_size $DEV_BATCH_SIZE \
    --gradient_accumulation_steps $GRAD_ACCUMULARION_STEPS \
    --max_steps $MAX_STEP \
    --logging_steps 1 \
    --save_steps $SAVE_INTERVAL \
    --learning_rate $LR \
    --pre_seq_len $PRE_SEQ_LEN 2>&1 | tee ${OUTPUT_DIR}/train.log
