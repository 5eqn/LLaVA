# Ensure train dataset folder exists
mkdir -p ./playground/data/train/flickr30k

# Convert Flickr30k dataset to compatible format for train dataset
python convert/flickr30k-train.py ~/.cache/lavis/flickr30k/annotations/train.json ./playground/data/train/flickr30k/train.json

# Link image to train dataset
ln -s ~/.cache/lavis/flickr30k/images/flickr30k-images playground/data/train/flickr30k/flickr30k-images
