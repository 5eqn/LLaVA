# Ensure eval dataset folder exists
mkdir -p ./playground/data/eval/flickr30k

# Convert Flickr30k dataset to compatible format for train dataset
python convert/flickr30k-train.py '../.cache/lavis/flickr30k/annotations/train.json' './playground/data/train.json'
python convert/flickr30k-eval.py '../.cache/lavis/flickr30k/annotations/test.json' './playground/data/eval/flickr30k/test.json'

# Link image to train and eval dataset
ln -s ~/.cache/lavis/flickr30k/images/flickr30k-images playground/data/flickr30k-images
ln -s ~/.cache/lavis/flickr30k/images/flickr30k-images playground/data/eval/flickr30k/flickr30k-images
