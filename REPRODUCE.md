## Merge LoRA Weight

### Flickr30k

```
python scripts/merge_lora_weights.py --model-path checkpoints/llava-v1.5-7b-flickr30k-lora --model-base liuhaotian/llava-v1.5-7b --save-model-path checkpoints/llava-v1.5-7b-flickr30k-merged/
```

### OKVQA

```
python scripts/merge_lora_weights.py --model-path checkpoints/llava-v1.5-7b-okvqa-lora --model-base liuhaotian/llava-v1.5-7b --save-model-path checkpoints/llava-v1.5-7b-okvqa-merged/
```

## Evaluate Fine-tuned Model

```
CKPT=llava-v1.5-7b-flickr30k bash scripts/v1_5/custom/
CKPT=llava-v1.5-7b-flickr30k-partial bash scripts/v1_5/custom/
CKPT=llava-v1.5-7b-flickr30k-merged bash scripts/v1_5/custom/
CKPT=llava-v1.5-7b-okvqa bash scripts/v1_5/custom/
CKPT=llava-v1.5-7b-okvqa-partial bash scripts/v1_5/custom/
CKPT=llava-v1.5-7b-okvqa-merged bash scripts/v1_5/custom/
```

## Evaluate VQAv2

1. Download VQAv2 dataset
2. Run `bash scripts/v1_5/eval/vqav2.sh`

## Evaluate VizWiz

1. Download VizWiz dataset
2. Run `bash scripts/v1_5/eval/vizwiz.sh`

## Evaluate OKVQA

1. Download [OKVQA dataset](https://okvqa.allenai.org/download.html) and unzip into `./playground/data/eval/okvqa`
2. Run `bash convert/okvqa-eval.sh`
3. Run `bash scripts/v1_5/eval/okvqa.sh`

## Evaluate Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `bash convert/flickr30k-eval.sh`
3. Run `bash scripts/v1_5/eval/flickr30k.sh`

## Finetune with OKVQA

1. Download [OKVQA dataset](https://okvqa.allenai.org/download.html) and unzip into `./playground/data/eval/okvqa`
2. Run `bash convert/okvqa-train.sh`
3. If GPU count `n` is 4, run `sed -i 's/--per_device_train_batch_size 16/--per_device_train_batch_size 32/' scripts/v1_5/finetune-okvqa.sh` and `sed -i 's/--per_device_train_batch_size 16/--per_device_train_batch_size 32/' scripts/v1_5/finetune-okvqa-lora.sh`
4. Run `bash scripts/v1_5/finetune-okvqa.sh` or `bash scripts/v1_5/finetune-okvqa-lora.sh`

## Finetune with Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `bash convert/flickr30k-train.sh`
3. If GPU count `n` is 4, run `sed -i 's/--per_device_train_batch_size 16/--per_device_train_batch_size 32/' scripts/v1_5/finetune-flickr30k.sh` and `sed -i 's/--per_device_train_batch_size 16/--per_device_train_batch_size 32/' scripts/v1_5/finetune-flickr30k-lora.sh`
4. Run `bash scripts/v1_5/finetune-flickr30k.sh` or `bash scripts/v1_5/finetune-flickr30k-lora.sh` or `bash scripts/v1_5/finetune-flickr30k-partial.sh`

## Quick Reinstall

```
pip config unset global.extra-index-url
pip uninstall llava
pip install --upgrade pip  # enable PEP 660 support
pip install -e .
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
```
