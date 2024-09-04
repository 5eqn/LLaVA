# Ensure train dataset folder exists
mkdir -p ./playground/data/train/okvqa

# Convert OKVQA dataset to compatible format for train dataset
python convert/okvqa-train.py ./playground/data/eval/okvqa/OpenEnded_mscoco_train2014_questions.json ./playground/data/eval/okvqa/mscoco_train2014_annotations.json ./playground/data/train/okvqa/train.json

# Link image to train dataset
ln -s ~/.cache/lavis/coco/images/train2014 ./playground/data/train/okvqa/train2014
