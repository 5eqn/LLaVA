## Preparation

1. Add extra PyTorch index: `pip config set global.extra-index-url https://download.pytorch.org/whl/cu118`

## Evaluate Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `python convert/flickr30k.py`
3. TODO generate test result with correct format

## Finetune with Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `bash convert/flickr30k.sh`
3. Get pretrained projector weight with `git clone https://huggingface.co/liuhaotian/llava-v1.5-mlp2x-336px-pretrain-vicuna-7b-v1.5` at home directory
4. Run `bash scripts/v1_5/finetune-flickr30k.sh`
