## Preparation

1. Add extra PyTorch index: `pip config set global.extra-index-url https://download.pytorch.org/whl/cu118`

## Evaluate VQAv2

1. Download VQAv2 dataset
2. Run `bash scripts/v1_5/eval/vqav2.sh`
3. (For fine-tuned) Run `bash scripts/v1_5/eval/vqav2-flickr30k.sh`

## Evaluate Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `python convert/flickr30k.sh`
3. Run `bash scripts/v1_5/eval/flickr30k.py`

## Finetune with Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `bash convert/flickr30k.sh`
3. Get pretrained projector weight with `git clone https://huggingface.co/liuhaotian/llava-v1.5-mlp2x-336px-pretrain-vicuna-7b-v1.5` at home directory
4. If GPU count `n` is 4, run `sed -i 's/--per_device_train_batch_size 16/--per_device_train_batch_size 32/' scripts/v1_5/finetune-flickr30k.sh`
5. Run `bash scripts/v1_5/finetune-flickr30k.sh`
6. (For LoRA) Run `bash scripts/v1_5/finetune-flickr30k-lora.sh`

## Quick reinstall

```
pip config unset global.extra-index-url
pip uninstall llava
pip install --upgrade pip  # enable PEP 660 support
pip install -e .
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
```
