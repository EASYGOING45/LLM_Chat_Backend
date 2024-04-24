deepspeed --num_gpus=2 --master_port 42 train.py \
    --model_name_or_path bigscience/bloom-560m \
    --data_path data_proj/opendata \
    --bf16 False \
    --output_dir output_dir \
    --num_train_epochs 3 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 2000 \
    --save_total_limit 1 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --deepspeed "./configs/default_offlload_zero2.json" \
    --tf32 False