You are a experienced programmer using Linux. Please write a Python script according to given environment and task.

## Environment

Content of `../.cache/lavis/flickr30k/annotations/test.json`:

```json
[{"image": "flickr30k-images/1007129816.jpg", "caption": ["The man with pierced ears is w
earing glasses and an orange hat.", "A man with glasses is wearing a beer can crocheted h
at.", "A man with gauges and glasses is wearing a Blitz hat.", "A man in an orange hat st
arring at something.", "A man wears an orange hat and glasses."]}, {"image": "flickr30k-i
mages/1009434119.jpg", "caption": ["A black and white dog is running in a grassy garden s
urrounded by a white fence.", "A Boston Terrier is running on lush green grass in front o
f a white fence.", "A black and white dog is running through the grass.", "A dog runs on
the green grass near a wooden fence.", "A Boston terrier is running in the grass."]}, {"i
mage": "flickr30k-images/101362133.jpg", "caption": ["A young female student performing a
 downward kick to break a board held by her Karate instructor.", "Girl about to kick a pi
ece of wood in half while karate instructor holds it", "A girl kicking a stick that a man
 is holding in tae kwon do class.", "A girl in karate uniform breaking a stick with a fro
nt kick.", "A girl breaking boards by using karate."]}, ...]
```

## Task

Your Python script should convert the above JSON to `./test.json` with format below:

```json
[
  {
    "id": "997bb945-628d-4724-b370-b84de974a19f",
    "image": "part-000001/997bb945-628d-4724-b370-b84de974a19f.jpg",
    "conversations": [
      {
        "from": "human",
        "value": "<image>\nWrite a prompt for Stable Diffusion to generate this image."
      },
      {
        "from": "gpt",
        "value": "a beautiful painting of chernobyl by nekro, pascal blanche, john harris, greg rutkowski, sin jong hun, moebius, simon stalenhag. in style of cg art. ray tracing. cel shading. hyper detailed. realistic. ue 5. maya. octane render. "
      },
    ]
  },
  ...
]
```

Where:

- `id` is a unique UUID assigned to each test case.
- `image` should be unchanged.
- `conversations` are expected conversation for this test case.
	- The first message's content should be read from a `PROMPT` variable in the script.
	- The second message's content should be concatenated from captions.

## I/O

Input: `../.cache/lavis/flickr30k/annotations/test.json`
Output: `./test.json`
