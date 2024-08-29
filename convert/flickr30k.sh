# Convert Flickr30k dataset to compatible format for train dataset
python convert/flickr30k-train.py '../.cache/lavis/flickr30k/annotations/train.json' './playground/data/train.json'
# python convert/flickr30k.py --input_file='../.cache/lavis/flickr30k/annotations/val.json' --output_file='./playground/data/val.json'
# python convert/flickr30k.py --input_file='../.cache/lavis/flickr30k/annotations/test.json' --output_file='./playground/data/test.json'

# Copy required annotations to eval dataset
# TODO eval questions have different format
# mkdir -p ./playground/data/eval/flickr30k
# cp ./playground/data/*.json ./playground/data/eval/flickr30k/

# Link image to train and eval dataset
ln -s ~/.cache/lavis/flickr30k/images/flickr30k-images playground/data/flickr30k-images
# ln -s ~/.cache/lavis/flickr30k/images/flickr30k-images playground/data/eval/flickr30k/flickr30k-images
