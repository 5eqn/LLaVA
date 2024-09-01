#!/bin/bash

gpu_list="${CUDA_VISIBLE_DEVICES:-0}"
IFS=',' read -ra GPULIST <<< "$gpu_list"

CHUNKS=${#GPULIST[@]}

CKPT="llava-v1.5-7b-flickr30k"
SPLIT="flickr30k"

for IDX in $(seq 0 $((CHUNKS-1))); do
    CUDA_VISIBLE_DEVICES=${GPULIST[$IDX]} python -m llava.eval.model_vqa_loader \
        --model-path ./checkpoints/$CKPT \
        --question-file ./playground/data/eval/flickr30k/test.jsonl \
        --image-folder ./playground/data/eval/flickr30k \
        --answers-file ./playground/data/eval/flickr30k/answers/$SPLIT/$CKPT/${CHUNKS}_${IDX}.jsonl \
        --num-chunks $CHUNKS \
        --chunk-idx $IDX \
        --temperature 0 \
        --conv-mode vicuna_v1 &
done

wait

output_file=./playground/data/eval/flickr30k/answers/$SPLIT/$CKPT/merge.jsonl

# Clear out the output file if it exists.
> "$output_file"

# Loop through the indices and concatenate each file.
for IDX in $(seq 0 $((CHUNKS-1))); do
    cat ./playground/data/eval/flickr30k/answers/$SPLIT/$CKPT/${CHUNKS}_${IDX}.jsonl >> "$output_file"
done

python convert/flickr30k-cider.py ~/.cache/lavis/flickr30k/annotations/test.json ./playground/data/eval/flickr30k/test.jsonl ./playground/data/eval/flickr30k/answers/flickr30k/llava-v1.5-7b-flickr30k/merge.jsonl
