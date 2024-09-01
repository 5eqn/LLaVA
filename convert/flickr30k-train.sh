# Convert Flickr30k dataset to compatible format for train dataset
python convert/flickr30k-train.py '~/.cache/lavis/flickr30k/annotations/train.json' './playground/data/train.json'

# Link image to train and eval dataset
ln -s ~/.cache/lavis/flickr30k/images/flickr30k-images playground/data/flickr30k-images
