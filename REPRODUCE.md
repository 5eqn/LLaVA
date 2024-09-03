## Evaluate VQAv2

1. Download VQAv2 dataset
2. Run `bash scripts/v1_5/eval/vqav2.sh` or `bash scripts/v1_5/eval_finetuned/vqav2.sh`

## Evaluate VizWiz

1. Download VizWiz dataset
2. Run `bash scripts/v1_5/eval/vizwiz.sh` or `bash scripts/v1_5/eval_finetuned/vizwiz.sh`

## Evaluate OKVQA

1. Download [OKVQA dataset](https://okvqa.allenai.org/download.html)
2. Run `bash convert/okvqa-eval.sh`
3. Run `bash scripts/v1_5/eval/okvqa.sh`
4. Evaluate according to `https://github.com/GT-Vision-Lab/VQA/blob/master/README.md`

## Evaluate Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `bash convert/flickr30k-eval.sh`
3. Run `bash scripts/v1_5/eval/flickr30k.sh` or `bash scripts/v1_5/eval_finetuned/flickr30k.sh` or `bash scripts/v1_5/eval_finetuned_lora/flickr30k.sh`

## Finetune with Flickr30k

1. Download Flickr30k dataset with automatic download tool in LAVIS repo
2. Run `bash convert/flickr30k-train.sh`
3. Get pretrained projector weight with `git clone https://huggingface.co/liuhaotian/llava-v1.5-mlp2x-336px-pretrain-vicuna-7b-v1.5` at `../` directory
4. If GPU count `n` is 4, run `sed -i 's/--per_device_train_batch_size 16/--per_device_train_batch_size 32/' scripts/v1_5/finetune-flickr30k.sh`
5. Run `bash scripts/v1_5/finetune-flickr30k.sh` or `bash scripts/v1_5/finetune-flickr30k-lora.sh`

## Quick Reinstall

```
pip config unset global.extra-index-url
pip uninstall llava
pip install --upgrade pip  # enable PEP 660 support
pip install -e .
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
```
