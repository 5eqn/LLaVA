You are a experienced programmer using Linux. Please write a Python script according to given environment and task.

## Environment

Content of `../.cache/lavis/flickr30k/annotations/test.json`:

```json
[
    {
        "image": "flickr30k-images/1007129816.jpg",
        "caption": [
            "The man with pierced ears is wearing glasses and an orange hat.",
            "A man with glasses is wearing a beer can crocheted hat.",
            "A man with gauges and glasses is wearing a Blitz hat.",
            "A man in an orange hat starring at something.",
            "A man wears an orange hat and glasses."
        ]
    },
    {
        "image": "flickr30k-images/1009434119.jpg",
        "caption": [
            "A black and white dog is running in a grassy garden surrounded by a white fence.",
            "A Boston Terrier is running on lush green grass in front of a white fence.",
            "A black and white dog is running through the grass.",
            "A dog runs onthe green grass near a wooden fence.",
            "A Boston terrier is running in the grass."
        ]
    },
    {
        "image": "flickr30k-images/101362133.jpg",
        "caption": [
            "A young female student performing a downward kick to break a board held by her Karate instructor.",
            "Girl about to kick a piece of wood in half while karate instructor holds it",
            "A girl kicking a stick that a man is holding in tae kwon do class.",
            "A girl in karate uniform breaking a stick with a front kick.",
            "A girl breaking boards by using karate."
        ]
    },
    ...
]
```

## Task

Your Python script should convert the above JSON to `./test.json` with format below:

```json
[
    {
        "id": "997bb945-628d-4724-b370-b84de974a19f",
        "image": "flickr30k-images/1007129816.jpg",
        "conversations": [
            {
                "from": "human",
                "value": "<image>\nA short image caption."
            },
            {
                "from": "gpt",
                "value": "The man with pierced ears is wearing glasses and an orange hat."
            },
        ]
    },
  ...
]
```

You create 5 test cases for each image. For test case `i`:

- `id` is a unique UUID assigned to each test case.
- `image` should be unchanged.
- `conversations` are expected conversation for this test case.
	- The first message's content is constant over all conversations.
	- The second message's content should be `annotations[i]`.

## I/O

Input: `../.cache/lavis/flickr30k/annotations/test.json`
Output: `./test.json`
