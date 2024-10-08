#!/bin/bash

gpu_list="${CUDA_VISIBLE_DEVICES:-0}"
IFS=',' read -ra GPULIST <<< "$gpu_list"

CHUNKS=${#GPULIST[@]}

# CKPT="llava-v1.5-7b"
SPLIT="okvqa"

for IDX in $(seq 0 $((CHUNKS-1))); do
    CUDA_VISIBLE_DEVICES=${GPULIST[$IDX]} python -m llava.eval.model_vqa_loader \
        --model-path ./checkpoints/$CKPT \
        --question-file ./playground/data/eval/okvqa/test.jsonl \
        --image-folder ./playground/data/eval/okvqa/val2014 \
        --answers-file ./playground/data/eval/okvqa/answers/$SPLIT/$CKPT/${CHUNKS}_${IDX}.jsonl \
        --max_new_tokens 128 \
        --num-chunks $CHUNKS \
        --chunk-idx $IDX \
        --temperature 0 \
        --conv-mode vicuna_v1 &
done

wait

output_file=./playground/data/eval/okvqa/answers/$SPLIT/$CKPT/merge.jsonl

# Clear out the output file if it exists.
> "$output_file"

# Loop through the indices and concatenate each file.
for IDX in $(seq 0 $((CHUNKS-1))); do
    cat ./playground/data/eval/okvqa/answers/$SPLIT/$CKPT/${CHUNKS}_${IDX}.jsonl >> "$output_file"
done

echo "Convert OKVQA for submission..."
python scripts/convert_okvqa_for_submission.py --split $SPLIT --ckpt $CKPT
echo "Evaluating VQA score..."
python scripts/vqaEvalDemo.py $CKPT
