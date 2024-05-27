#! /usr/bin/env bash


source activate py310_chat
cd /root/ChatGLM3/finetune_chatmodel_demo

set -ex

PRE_SEQ_LEN=128
LR=2e-2
NUM_GPUS=1
MAX_SOURCE_LEN=1028
MAX_TARGET_LEN=128
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=32
MAX_STEP=1000
SAVE_INTERVAL=50
RUN_NAME=模型
BASE_MODEL_PATH=/root/autodl-tmp/chatglm3-6b
DATASET_PATH=/root/微调地点/单轮.jsonl

DATESTR=$(date +%s)

OUTPUT_DIR_NAME=${RUN_NAME}-${DATESTR}
OUTPUT_DIR=/root/微调地点/output/${OUTPUT_DIR_NAME}

mkdir -p /root/ChatGLM3/finetune_chatmodel_demo/hhh/
echo $OUTPUT_DIR_NAME > /root/ChatGLM3/finetune_chatmodel_demo/hhh/hhh.txt

mkdir -p $OUTPUT_DIR

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
