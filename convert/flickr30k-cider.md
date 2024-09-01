You are a experienced programmer using Linux. Please write a Python script according to given environment and task.

## Environment

Content of ground truth `~/.cache/lavis/flickr30k/annotations/test.json`:

```csv
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

Content of question `./playground/data/eval/flickr30k/test.jsonl`:

```
{"question_id": 262144005, "image": "COCO_test2015_000000262144.jpg", "text": "What credi
t card company is on the banner in the background?\nAnswer the question using a single wo
rd or phrase.", "category": "default"}
{"question_id": 262144003, "image": "COCO_test2015_000000262144.jpg", "text": "Is the pit
cher wearing a hat?\nAnswer the question using a single word or phrase.", "category": "de
fault"}
{"question_id": 262144000, "image": "COCO_test2015_000000262144.jpg", "text": "Is the bal
l flying towards the batter?\nAnswer the question using a single word or phrase.", "categ
ory": "default"}
```

Content of answer `./playground/data/eval/flickr30k/answers/flickr30k/llava-v1.5-7b/merge.jsonl`:

```
{"question_id": 262144005, "prompt": "What credit card company is on the banner in the ba
ckground?\nAnswer the question using a single word or phrase.", "text": "Mastercard", "an
swer_id": "Nkgs9ckMfp3aPdrR8pf7DQ", "model_id": "llava-v1.5-7b", "metadata": {}}
{"question_id": 262144003, "prompt": "Is the pitcher wearing a hat?\nAnswer the question
using a single word or phrase.", "text": "Yes", "answer_id": "h3vKaP2DUhkFZEArPuAaUc", "m
odel_id": "llava-v1.5-7b", "metadata": {}}
{"question_id": 262144000, "prompt": "Is the ball flying towards the batter?\nAnswer the
question using a single word or phrase.", "text": "No", "answer_id": "dzLSh7hu4C2dbgUa6gk
c7V", "model_id": "llava-v1.5-7b", "metadata": {}}
```

## Task

Your Python script should calculate CIDEr score with answer and grount truth. An example of using CIDEr is:

```py
from .cider import CiderScorer
with open(answer_path, 'r') as f:
    dict = json.load(f)
    cider_scorer = CiderScorer(n=4, sigma=6.0)
    for i in range(len(dict)):
        gt_answers = dict[i]['gt_answers']
        answer = dict[i]['answer']
        cider_scorer += (answer, gt_answers)
    (score, scores) = cider_scorer.compute_score()
```

You should change the example usage according to actual requirements.

Note that `gt_answers` has multiple entries. You should get `gt_answers` by getting `question_id` in answer file, then get `image` from question file, then get all 5 comments from grount truth.

You should read all paths from command line arguments.
