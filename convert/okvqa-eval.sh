# Ensure eval dataset folder exists
mkdir -p ./playground/data/eval/okvqa

# Convert OKVQA dataset to compatible format for eval dataset
python convert/okvqa-eval.py ./playground/data/eval/okvqa/OpenEnded_mscoco_val2014_questions.json ./playground/data/eval/okvqa/test.jsonl

# Link image to eval dataset
ln -s ~/.cache/lavis/coco/images/val2014 ./playground/data/eval/okvqa/val2014
